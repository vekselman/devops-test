import sys
import glob
import os
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# Construct a portable wildcard pattern
pattern = hdir + os.sep + "*"
# Use the glob.glob() function to obtain the list of filenames
for filename in glob.glob(pattern):
# Use os.path.getsize to find each file's size
    if os.path.getsize(filename) > 0:
        # print(os.path.basename(filename), os.path.getsize(filename))
        print(os.path.abspath(filename), os.path.getsize(filename))
# Only display files that are not zero length
