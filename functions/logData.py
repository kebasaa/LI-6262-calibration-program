# This function logs all collected data to a csv file for later.
# It will be easier to have it in a function

from os.path import expanduser
home = expanduser("~")

def logData(logFile, data, header):
	if(header == 1):
            my_file = open(home + '/' + logFile,'w') # Overwrite existing data if it's there
            my_file.write('Date,RH.out,T.out,HI.out,P.out,L.out,RH.in,T.in,HI.in,L.in,D.in,AC.on,HU.on,T.cpu,PRC.cpu,PRC.ram,PRC.disk\n')
	else:
            my_file = open(home + '/' + logFile,'a')
            csvString = data[0] + ',' + str(data[1]) + ',' + str(data[2]) + ',' + str(data[3]) + ',' + str(data[4]) + ',' + str(data[5]) + ',' + str(data[6]) + ',' + str(data[7]) + ',' + str(data[8]) + ',' + str(data[9]) + ',' + str(data[10]) + ',' + str(data[11]) +',' + str(data[12]) + ',' + str(data[13]) + ',' + str(data[14]) + ',' + str(data[15]) + ',' + str(data[16]) + '\n'
            '''
            csvString = data[0] + ',' + # Current date & time
                        str(data[1]) + ',' +    # RH.out
                        str(data[2]) + ',' +    # T.out
                        str(data[3]) + ',' +	# HI.out (calculated)
                        str(data[4]) + ',' +	# P.out
                        str(data[5]) + ',' +	# L.out
                        str(data[6]) + ',' +	# RH.in
                        str(data[7]) + ',' +	# T.in
                        str(data[8]) + ',' +	# HI.in (calculated)
                        str(data[9]) + ',' +	# L.in  (calculated from arduino voltage reading)
                        str(data[10]) + ',' +	# D.in
                        str(data[11]) + ',' +   # AC.on
                        str(data[12]) + ',' +	# HU.on (humidifier)
                        str(data[13]) + ',' +   # rPi CPU temperature
                        str(data[14]) + ',' +   # rPi CPU usage %
                        str(data[15]) + ',' +   # rPi RAM usage %
                        str(data[16]) + '\n')   # rPi disk usage %
            '''
            my_file.write(csvString)
	my_file.close()
	return(0)
