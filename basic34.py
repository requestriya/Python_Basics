# wap to determine if a python shell is executing in 32bit OR 64bit mode on OS

import struct, platform

print(platform.architecture())
print(platform.architecture()[0])