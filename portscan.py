import os, socket

DSTIP="169.254.79.2"

def lambda_handler(event, context):
    for DSTPORT in range(0,10):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((DSTIP, DSTPORT))
            print "Connection accepted on port %s!" % DSTPORT
            print s.recv(4096)
        except:
            print "Connection refused on port %s!" % DSTPORT
