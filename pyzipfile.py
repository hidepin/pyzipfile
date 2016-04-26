#!/usr/bin/env python

import pyminizip
import threading

zipnamelist = list(range(10000))

def compress(zipnamelist):
    while True:
        pyminizip.compress("hoge", str(zipnamelist.pop()) + ".zip", "password", 6)

for i in range(1):
    thread = threading.Thread(target=compress, args=(zipnamelist,))
    thread.start()
