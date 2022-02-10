import os
class Config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or b'\xd6o\xb0l\xe24y\xaag\xa3G\xd0\xc5\xe7h\x08'
    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}
