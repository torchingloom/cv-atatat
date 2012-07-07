# -*- coding: utf-8 -*-

import socket
if 'cittavita' in socket.gethostname():
    from config.settings_by_env.production import *
else:
    from config.settings_by_env.dev import *

