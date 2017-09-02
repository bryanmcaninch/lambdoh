import os
import socket

def lambda_handler(event, context):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("169.254.79.2", 2000))
        print "Connection accepted!"
        print s.recv(4096)
    except:
        print "Connection refused!"
