#-------------------------------------------------------------------------------
# Name:        LI-COR control software
# Purpose:	   This software automatically calibrates the LI-7000
#
# Author:      Jonathan D. Müller
#
# Created:     29/09/2016
# Copyright:   (c) Jonathan D. Müller 2016
# Licence:     GPL
#-------------------------------------------------------------------------------

# System stuff
import serial, sys
import ctypes # Needed to tell Windows to use my icon
import datetime
import json # used to parse config.json
import signal # for signals between threads
from time import strftime # For logging

# Import Qt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Import the user interface
from Interface import *
import functions.listCOM
serial_ports = functions.listCOM.serial_ports
import functions.serialThread
serialThread = functions.serialThread.serialThread
import functions.li6262
li6262Thread = functions.li6262.li6262Thread

# Logging
import logging
import sys
log = logging.getLogger('root')
log.setLevel(logging.DEBUG)
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)8s %(module)15s: %(message)s')
stream.setFormatter(formatter)
log.addHandler(stream)

class Main(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        log.info("Starting LI-6262 program")
        # initialise the data list
        self.data = [None]*5
        # These threads run in the background
        self.initUI()
        self.initThreads()

    def initThreads(self):
        #self.addLogFile()
        
        self.li6262_running = False
        
        # Update every second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timed_tasks)
        self.timer.start(1000)

    def initUI(self):
        # Check for COM ports and add them
        self.addCOM()
        self.get_config() # where to save the calibration log
        self.ui.connectLI6262.clicked.connect(self.connectLI6262)
        self.ui.CO2Zero.clicked.connect(self.CO2Zero)
        self.ui.H2OZero.clicked.connect(self.H2OZero)
        self.ui.CO2Span.clicked.connect(self.CO2Span)
        self.ui.H2OSpan.clicked.connect(self.H2OSpan)
		
    def get_config(self):
        with open('settings.json') as config_file:
            self.config = json.load(config_file)

    def timed_tasks(self):
        self.update_label()

    def collect_data(self):
        self.data[0] = strftime("%Y-%m-%d %H:%M:%S")		# Date and time
        log.info(self.data)
        # LI-6262
        try:
            self.data[1] = self.li6262.data[0]
        except:
            self.data[1] = float('nan')		# CO2 (umol/mol)
            self.data[2] = float('nan')		# H2O (mmol/mol)
            self.data[3] = float('nan')		# ?
            self.data[4] = float('nan')		# ? ()
        else:
            self.data[1] = self.li6262.data[0] # CO2 (umol/mol)
            self.data[2] = self.li6262.data[1] # H2O (mmol/mol)
            self.data[3] = self.li6262.data[2] # ?
            self.data[4] = self.li6262.data[3] # ? ()

    def isNaN(num):
        return num != num
        
    def update_label(self):
        # LI-6262
        try:
            self.li6262_co2 = self.li6262.data[0]
            self.li6262_h2o = self.li6262.data[1]
        except:
            self.ui.co2.setText("")
            self.ui.h2o.setText("")
        else:
            self.ui.co2.setText("{:.3f}".format(self.li6262_co2))
            self.ui.h2o.setText("{:.3f}".format(self.li6262_h2o))
		
    def connectLI6262(self):
        if(self.li6262_running == True):
            log.info("Disconnecting LI-6262")
            self.li6262.stop()
            del self.li6262
            self.ui.connectLI6262.setText("Connect")
            self.li6262_running = False
        else:
            log.info("Connecting LI-6262")
            port = self.COM["device"][self.ui.COM_LI6262.currentIndex()]
            self.li6262 = li6262Thread(port)
            self.li6262.start()
            self.ui.connectLI6262.setText("Disconnect")
            self.li6262_running = True
		
    def CO2Zero(self):
        log.info("co2 zero")
        self.li6262.zeroCO2()
		
    def H2OZero(self):
        log.info("h2o zero")
        self.li6262.zeroH2O()
		
    def CO2Span(self):
        log.info("co2 span")
        self.li6262.spanCO2(int(self.ui.CO2SpanVal.text()))
        # CO2SpanVal
		
    def H2OSpan(self):
        log.info("h2o span")
        self.li6262.spanH2O(int(self.ui.H2OSpanVal.text()), 101.3) # second value is barometric P
        # H2OSpanVal
			
    def addCOM(self): # Adds COM ports to the list
        #log.debug("Checking COM ports...")
        # Check COM ports
        self.COM = serial_ports()
        x = 0
        for port in self.COM["device"]:
            self.ui.COM_LI6262.addItem(str(port + " - " + self.COM["name"][x]))
            x += 1
			
    def addLogFile(self):
        logfile = logging.FileHandler(self.config["match_log"])
        logfile.setLevel(logging.DEBUG)
        logfile.setFormatter(formatter)
        log.addHandler(logfile)
        pass
			
    def closeEvent(self, event): # This is when the window is clicked to close
        self.closeThreads()
        event.accept()
		
    # When the program ends, we want to save the settings
    def set_config(self):
        self.config["co2_span"] = int(self.ui.CO2SpanVal.text())
        self.config["h2o_span"] = int(self.ui.H2OSpanVal.text())
        with open('settings.json', 'w') as cfile:
            cfile.write(json.dumps(self.config))
			
    def closeThreads(self):
        # User wants to close the application.
		# Because of this, we need to shut down all running background threads
        log.info("Shutting down application")
        try: self.li6262.stop()
        except: pass
        #self.set_config()
        log.info("Shutdown completed")
        log.info('------------------')
		
# Show the image
if __name__ == "__main__":
    # This tells Windows to use my icon
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	
    app = QApplication(sys.argv)
    myapp = Main()
    myapp.show()
	
    sys.exit(app.exec_())