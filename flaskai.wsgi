#!/usr/bin/python
activate_this = '/home/tangyu/anaconda3/envs/keras1_tf1/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/flask_ai/")
from flask_ssd import app as application