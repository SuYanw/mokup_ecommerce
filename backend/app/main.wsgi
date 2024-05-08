#!/usr/bin/python3.8
import os
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/")

from main import app as application