#!/usr/bin/env python

import subprocess
import time
import os

from gpiozero import OutputDevice


ON_THRESHOLD = 55.0  # (degrees Celsius) Fan kicks on at this temperature.
OFF_THRESHOLD = 40.0  # (degress Celsius) Fan shuts off at this temperature.
SLEEP_INTERVAL = 5  # (seconds) How often we check the core temperature.
GPIO_PIN = 18  # Which GPIO pin you're using to control the fan.


def get_temp():
    """Get the core temperature.

    Run a shell script to get the core temp and parse the output.

    Raises:
        RuntimeError: if response cannot be parsed.

    Returns:
        float: The core temperature in degrees Celsius.
    """
    output = os.popen("vcgencmd measure_temp").readline()
    try:
        return float(output.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not parse temperature output.')


if __name__ == '__main__':
    # Validate the on and off thresholds
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    fan = OutputDevice(GPIO_PIN)

    value = False
    while True:
        temp = get_temp()

        # Start the fan if the temperature has reached the limit and the fan
        # isn't already running.
        # fan.value` returns 1 for "on" and 0 for "off"
        if temp > ON_THRESHOLD and not value:
            fan.on()
            value = True

        # Stop the fan if the fan is running and the temperature has dropped
        # to 10 degrees below the limit.
        elif value and temp < OFF_THRESHOLD:
            fan.off()
            value = False

        print("temp={}\nfan={}\n".format(temp, value))
        time.sleep(SLEEP_INTERVAL)
