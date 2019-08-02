#! /usr/bin/python3.6
      
import logging
import sys
from app import app
import os

print(os.getcwd())

logging.basicConfig(stream=sys.stderr)
application.secret_key = 'anything you wish'