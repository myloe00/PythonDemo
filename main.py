import sys,os
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), 'plugin'))
from plugin.subProjectdemo.main.main import get_datasource

if __name__ == '__main__':
    print(get_datasource())
