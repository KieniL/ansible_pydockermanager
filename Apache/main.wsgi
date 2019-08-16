#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/dockermanager/')
from main import app as application
application.secret_key = b'_5#y2L"F4Q8z\n\xec]/'