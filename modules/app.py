print "this is app"
import sys
#sys.path.append("/home/khyaathi-python/Desktop")
sys.path.insert(1, "/home/khyaathi-python/Desktop")
print sys.path
import file1
print file1.__file__
