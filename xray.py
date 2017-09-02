import os, socket

DSTIP="169.254.79.2"
DSTPORT="2000"

def lambda_handler(event, context):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((DSTIP, DSTPORT))
        print "Connection accepted!"
        print s.recv(4096)
    except:
        print "Connection refused!"
