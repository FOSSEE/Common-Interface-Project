import os

# The location to keep the session data on server.
SESSIONDIR = '/tmp/sessiondir'
IMAGEDIR = 'images'
SESSIONTIMEOUT = 21600

# the instances

SCILAB_MIN_INSTANCES = int(os.environ.get('SCILAB_MIN_INSTANCES', '1'))
SCILAB_START_INSTANCES = int(os.environ.get('SCILAB_START_INSTANCES', '2'))
SCILAB_MAX_INSTANCES = int(os.environ.get('SCILAB_MAX_INSTANCES', '3'))
SCILAB_INSTANCE_RETRY_INTERVAL = int(os.environ.get('SCILAB_INSTANCE_RETRY_INTERVAL', '5'))
