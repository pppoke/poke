# Author:Game_bu

import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

school_add = ('北京', '上海')

course_type = ('python', 'go', 'linux')

accounts = {'admin': 'admin'}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'service': 'server.log',
    'system': 'access.log',
}