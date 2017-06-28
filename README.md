# LI-6262 calibration program

This program is based on Python 3 and can be used to calibrate a LI-COR LI-6262 IRGA gas analyser. Note that the IRGA needs to be set up properly before usage:

Press Fct 13 to set the channels
P. D-1 for channel codes. Check channel codes in the device manual
22
32
38
42

Press Fct 15 for header line: Set 0 to disable (otherwise the program will crash)
Press Fct 14 for update interval: Set to 1s

Requirements: Install modules
-----------------------------
pip3 install PyQt5 pyserial telepot

To convert .ui (Qt Designer file) to .py
----------------------------------------
pyuic5 -o Interface.py Interface.ui



