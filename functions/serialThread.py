import serial
from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal

import logging
log = logging.getLogger('root')

class serialThread(QThread):
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
    '''
    def matchCells(self):
        # Match water
        self.serialDevice.write('(UserCal(H2O(MatchNow)))')
        # Match CO2
        self.serialDevice.write('(UserCal(CO2(MatchNow)))')
    '''
    def processData(self):
        self.data = self.__rawdata.decode().split()
        self.data = [float(x) for x in self.data]
        #self.data = [round(x, 2) for x in self.data]

    def stop(self):
        log.info('Closing {} port'.format(self.port))
        self.serialDevice.close()
        self.__stopping=True	