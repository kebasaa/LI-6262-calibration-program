# LI-6262 calibration program

This program is based on Python 3 on Windows and can be used to calibrate a LI-COR LI-6262 IRGA gas analyser. It shouldn't be difficult to port to other systems Note that the IRGA needs to be set up properly before usage:

Press **Fct 13** to set the channels (Check channel codes in the [device manual](http://www.aoml.noaa.gov/ocd/ocdweb/brown/Licor_6262_Manual.pdf)):
* 22 (mandatory)
* 32 (mandatory)
* 38 (user choice)
* 42 (user choice)

Press **Fct 15** for header line: Set to **0 to disable** (otherwise the program will crash)

Press **Fct 14** for update interval: Set to **1s** (or any preferred interval)

## Requirements: Install modules

In the command window, enter:

    pip3 install PyQt5 pyserial telepot

## To convert .ui (Qt Designer file) to .py

In the command window, enter:

    pyuic5 -o Interface.py Interface.ui

## License

### Software

This software is distributed under the GPL version 3.

### Logos and icons

All logos and icons are trademark of [LI-COR Biosciences](https://www.licor.com/).
