import serial
import time

serialport = serial.Serial(port = "/dev/ttyAMA0",
				 baudrate=9600,parity=serial.PARITY_NONE,
				 stopbits=serial.STOPBITS_ONE,
				 bytesize=serial.EIGHTBITS,timeout=3.0)

while True:
	inputParameters = list()	
	#serialport.write("Hello World")
	serialport.flushInput()
	rcv = serialport.read(6)
#	print(repr(rcv))
#	i = int(repr(rcv).encode('hex'), 16)
	stringConverted = repr(rcv).decode("utf-8")
	listBytes=stringConverted.strip().split('\\x')
	i = 0
	#print(len(listBytes))
	while(i < len(listBytes) and listBytes[i] != "'A"):
		i+=1
	j = 0
	for j in range(len(listBytes)):
		if(i >= len(listBytes)):
			i = 0
		if(listBytes[i] != "'" or listBytes[i] != "'A"):
			inputParameters.append((listBytes[i]))
		
		i+=1
	for j in range(len(inputParameters)):
		if(len(inputParameters[j]) == 3):
			inputParameters[j] = inputParameters[j][0:2]
		print(inputParameters[j])
	print('\n')
