import serial
import time

serialport = serial.Serial(port = "/dev/ttyAMA0",
				 baudrate=9600,parity=serial.PARITY_NONE,
				 stopbits=serial.STOPBITS_ONE,
				 bytesize=serial.EIGHTBITS,timeout=3.0)

while True:
	rcv = serialport.read(8)
	print(repr(rcv))
	time.sleep(1)
