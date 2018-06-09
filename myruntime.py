import os, sys

def lambda_handler(event, context):
    print "DEBUG: lambda_handler"
    f = open('/tmp/logging.py', 'w+')
    f.write('print "DEBUG: inside execfile"')
    f.close
    f = open('/tmp/logging.py', 'r+')
    print "DEBUG: begin execfile"
    execfile('/tmp/logging.py')
    print "DEBUG: end execfile"
    f.close
