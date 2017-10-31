# Author:Game_bu

import os
import sys
import pickle

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import main
from conf import setting

if __name__ == '__main__':
    main.run()