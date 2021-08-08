# wap to access enivironment variables

import os

for data in os.environ:
    print(data)
    print('-'*15)
    print(os.environ[data])
    print('='*30)