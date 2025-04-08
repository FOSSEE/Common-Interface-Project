import os

# The location to keep the session data on server.
SESSIONDIR = '/tmp/sessiondir'
SESSIONTIMEOUT = 21600

# the instances

SCILAB_MIN_INSTANCES = int(os.environ.get('SCILAB_MIN_INSTANCES', '1'))
SCILAB_START_INSTANCES = int(os.environ.get('SCILAB_START_INSTANCES', '2'))
SCILAB_MAX_INSTANCES = int(os.environ.get('SCILAB_MAX_INSTANCES', '3'))
SCILAB_INSTANCE_RETRY_INTERVAL = int(os.environ.get('SCILAB_INSTANCE_RETRY_INTERVAL', '5'))

SCILAB_INSTANCE_TIMEOUT_INTERVAL = 300

# Following are system command which are not permitted in sci files
# (Reference scilab-on-cloud project)
SYSTEM_COMMANDS = (
    r'unix\(.*\)|unix_g\(.*\)|unix_w\(.*\)|unix_x\(.*\)|unix_s\(.*\)|host'
    r'|newfun|execstr|ascii|mputl|dir\(\)'
)
SPECIAL_CHARACTERS = r'["\'\\]'

# The directory where images are created
IMAGEDIR = 'images'

# Set CREATEIMAGE to True to create img_test.jpg in IMAGEDIR
CREATEIMAGE = False

REMOVEFILE = True
