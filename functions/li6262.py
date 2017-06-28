import serial
from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal

import logging
log = logging.getLogger('root')

class li6262Thread(QThread):
    def __init__(self,port):
        QThread.__init__(self)
		
        # Important variables
        self.port = port
        self.__rawdata = ""
        self.data = []
		
        # Signal to shut down
        self.__stopping=False
		
        self.port = "\\\\.\\" + self.port
        self.serialDevice = serial.Serial(self.port, 9600, timeout=2)
	
    def run(self):
        while True:
            try: self.__rawdata = self.serialDevice.readline()
            except: break
            self.processData()
            #log.info(self.data)
            if(self.__stopping):
                self.serialDevice.close()
                break
            else:
                sleep(1)
        log.debug("{} closing".format(self.port))

    # Calibration commands, LI-6262 manual, p. 4-11
    def zeroCO2(self):
        # Important: The same zero gas has to flow through both cells!
        self.serialDevice.write('*081,0,1,0\r\n'.encode("utf8"))

    def zeroH2O(self):
        # Important: The same zero gas has to flow through both cells!
        self.serialDevice.write('*082,0,1,0\r\n'.encode("utf8"))

    def spanCO2(self, CO2span):
        # The remote command sequence for the CO2 software zero and span is
        self.serialDevice.write(('*081,0,1,' + str(CO2span) + '\r\n').encode("utf8"))
		
    def spanH2O(self, H2Ospan, barometricP):
        dewpointTemp = H2Ospan
        if(barometricP == 0): barometricP = 101.3 # standard barometric pressure [kPa]
		
        # Manual p. 4-3: The water span needs the mole fraction
        H2OvaporP = 0.61083 * pow(10,((7.6448 * dewpointTemp)/(242.62 + dewpointTemp)))
        H2Ospan = 1000 * (H2OvaporP/barometricP)
		
        # The remote command sequence for the H2O software zero and span is
        self.serialDevice.write(('*082,0,1,' + str(H2Ospan) + '\r\n').encode("utf8"))

    def processData(self):
        self.data = self.__rawdata.decode().split()
        self.data = [float(x) for x in self.data]
        #self.data = [round(x, 2) for x in self.data]

    def stop(self):
        log.info('Closing {} port'.format(self.port))
        self.serialDevice.close()
        self.__stopping=True	