import serial
import time

serialport = serial.Serial(port = "/dev/ttyAMA0",
				 baudrate=9600,parity=serial.PARITY_NONE,
				 stopbits=serial.STOPBITS_ONE,
				 bytesize=serial.EIGHTBITS,timeout=3.0)

while True:
	serialport.write("Hello World")
	rcv = serialport.read(8)
	if(rcv[0] == 1){
		#turn off LCD
	}	
	elif(rcv[1] == 1){
		#PIR SENSOR, turn on LCD
	}
	print(repr(rcv))
	time.sleep(1)
