# see https://code.djangoproject.com/wiki/SplitSettings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'mydbname'
DATABASE_USER = 'mydbuser'
DATABASE_PASSWORD = 'mydbpassword'
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'THIS-IS-NOT-MY-REAL-SECRET-KEY'