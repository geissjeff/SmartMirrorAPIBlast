import serial

serialport = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

serialport.write("rnSay something:")
rcv = port.read(10)
serialport.write("rnYou sent:" + repr(rcv))
