#!/usr/bin/env python

import subprocess
import time
import os

from gpiozero import OutputDevice

GPIO_PIN = 18  # Which GPIO pin you're using to control the fan.

fan = OutputDevice(GPIO_PIN)
fan.off()
