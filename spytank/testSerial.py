import serial
from struct import pack, unpack

comm = serial.Serial()
comm.port = "/dev/ttyUSB0"
comm.baudrate = 9600
comm.open()
comm.write(pack('B',1))
print(comm.read())
#print( unpack('B',comm.read()) )
comm.close()