import hashlib
import os
from os.path import isdir, islink

for filename in os.listdir("."):
    if not isdir(filename) and not islink(filename):
        try:
            f = open(filename, "rb")
        except IOError as e:
            print(e)
        else:
            data = f.read()
            f.close()
            print("** %s **" % filename)                
            h = hashlib.new('sha1')
            h.update(data)
            try:
                hexdigest = h.hexdigest()
            except TypeError:
                hexdigest = h.hexdigest(128)
            print("%s: %s" % ('sha1', hexdigest))
            print()