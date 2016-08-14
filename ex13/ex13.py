#Unpacking - not in java or js or c or c++
#assign first argument to script then to first and so on...
#script, first, second, third = argv


from sys import argv

fileName, fa, sa, ta = argv

print 'fileName: ', fileName
print 'first variable is ', fa
print 'second variable is ', sa
print 'third variable is ', ta
# 
# Note: On giving less variables it will give
# error complaining less variable to unpack and
# on giving extra variables it will complain for
# extra variables
