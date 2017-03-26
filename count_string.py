#!/usr/bin/env python3
import os
import sys

s = sys.argv[1]
n = 0
for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        f = root+"/"+f      
        try:
            n = n + open(f).read().count(s)
        except:
            pass
print(n)
