# wap to get the path and name of the file that is currently executing

import os.path

print(os.path.realpath(__file__))
