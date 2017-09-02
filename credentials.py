import os

def lambda_handler(event, context):
    print "Access Key ID: %s\n" % os.getenv('AWS_ACCESS_KEY_ID')
    print "Access Key: %s\n" % os.getenv('AWS_SECRET_ACCESS_KEY')
    print "Security Token: %s\n" % os.getenv('AWS_SECURITY_TOKEN')
    print "Session Token: %s\n" % os.getenv('AWS_SESSION_TOKEN')
    return 0
