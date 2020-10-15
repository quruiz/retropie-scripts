# retropie-scripts

## Description

This repository provides scripts that can be run on the Raspberry Pi that will
shutdown the Raspberry Pi with a button and monitor the core temperature and start
the fan when the temperature reaches a certain threshold.

## Installation

1. [Connect to your Raspberry Pi via SSH](https://howchoo.com/g/mgi3mdnlnjq/how-to-log-in-to-a-raspberry-pi-via-ssh)
1. Clone this repo: `git clone https://github.com/quruiz/retropie-scripts.git`
1. If pip is not already installed run: `sudo apt install python3-pip`
1. Install requirements globally: `sudo pip3 install -r retropie-scripts/requirements.txt`
1. Run the setup script: `./retropie-scripts/script/install`

## Uninstallation

If you need to uninstall for another project or something:

1. Run the uninstall script: `./retropie-scripts/script/uninstall`

## Hardware

You'll need a normally-open (NO) power button, 5v fan, NPN transistor, some jumper wires and a soldering iron.

Connect the power button and the fan as shown in this diagram:

![Connection Diagram](https://raw.githubusercontent.com/quruiz/retropie-scripts/master/circuit.png)


### Is it possible to use another pin other than Pin 5 for the power button (GPIO 3/SCL)?

Not for full functionality, no. There are two main features of the power button:

1. **Shutdown functionality:** Shut the Pi down safely when the button is pressed. The Pi now consumes zero power.
1. **Wake functionality:** Turn the Pi back on when the button is pressed again.

The **wake functionality** requires the SCL pin, Pin 5 (GPIO 3). There's simply no other pin that can "hardware" wake the Pi from a zero-power state. If you don't care about turning the Pi back _on_ using the power button, you could use a different GPIO pin for the **shutdown functionality** and still have a working shutdown button. Then, to turn the Pi back on, you'll just need to disconnect and reconnect power (or use a cord with a physical switch in it) to "wake" the Pi.


### Is it possible change fan pin and temperature threshold ?

```python
ON_THRESHOLD = 65 
OFF_THRESHOLD = 55
SLEEP_INTERVAL = 5
GPIO_PIN = 18
```

These variables can be configured to your liking. ON_THRESHOLD and OFF_THRESHOLD are the temperatures at which the fan will turn on and off (respectively), and SLEEP_INTERVAL is how often the program checks the core temperature. If you need to change the GPIO pin, you can do that here as well.

Feel free to customize either of these variables, but keep in mind that the max temperature is 85C, and the CPU will be throttled at around 80C, so we'll want to keep the temperature well below that.


Of course, for the GND and 5v connection, you can use [any other pin you want](https://pinout.xyz/).
