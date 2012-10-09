
ENVIRONMENT = r'dev'

try:
    from _ENVIRONMENT import ENVIRONMENT
except ImportError:
    pass

if ENVIRONMENT == 'dev':
    from config.settings_by_env.dev import *
elif ENVIRONMENT == 'production':
    from config.settings_by_env.production import *

try:
    from settings_local import *
except ImportError:
    pass

