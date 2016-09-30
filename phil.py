#!/usr/bin/python

import socket, struct, argparse

# Arguments parser
parser = argparse.ArgumentParser(description='An X-Plane HIL interface.',
	                             epilog='Developed by GEPSE@UFSM.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-a', '--address', dest='IP', default='127.0.0.1',
                   help='server (X-Plane) IP address')
parser.add_argument('-p', '--port', dest='PORT', default=5000,
                   help='server (X-Plane) port')
parser.add_argument('-v', '--verbose', action='store_true',
                   default='True', dest='VERBOSE',
                   help='verbose mode, prints information to console')

args = parser.parse_args()

IP = args.IP
PORT = args.PORT
VERBOSE = args.VERBOSE

# Socket definition
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

def hex_format(data):
    return "".join("{:02x}".format(ord(c)) for c in data)  # [1]

def hex2float(data):
    return struct.unpack('!f', data.decode('hex'))[0]




while True:
    data, addr = socket.recvfrom(1024) # buffer (1024 bytes)

    header = data[:4]
    index  = data[5:9]
    parameters = data[9:]
    print "\n" + IP + ":" + str(PORT) + " >> [" + header + "][" + hex_format(index) + "]"
    param1 = (parameters[:4])[::-1]
    param2 = (parameters[4:8])[::-1]
    param3 = (parameters[8:12])[::-1]
    param4 = (parameters[12:16])[::-1]
    param5 = (parameters[16:20])[::-1]
    param6 = (parameters[20:24])[::-1]
    param7 = (parameters[24:28])[::-1]
    param8 = (parameters[28:32])[::-1]
 
    print hex_format(data)

    #print hex_format(param1) + "|" + hex_format(param2) + "|" + hex_format(param3) + "|" + hex_format(param4) + "|" + hex_format(param5) + "|" + hex_format(param6) + "|" + hex_format(param7) + "|" + hex_format(param8)

    #print str(hex2float(hex_format(param1))) + "\t" + str(hex2float(hex_format(param2))) + "\t" + str(hex2float(hex_format(param3))) + "\t" + str(hex2float(hex_format(param4))) + "\t" + str(hex2float(hex_format(param5))) + "\t" + str(hex2float(hex_format(param6))) + "\t" + str(hex2float(hex_format(param7))) + "\t" + str(hex2float(hex_format(param8)))    

# [0] http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
# [1] http://stackoverflow.com/questions/12214801/print-a-string-as-hex-bytes
