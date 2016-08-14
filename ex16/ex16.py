# cant use read commands as file is opened in
# write mode and when file is opend in write mode
# it auto gets truncated.

from sys import argv

pn, fn = argv

print "Goiing to do some fun stuff!"

print "opening your file"

file = open(fn, 'w')

#print file.readline()

#print file.readline()

line = raw_input("enter a line");
file.write(line)
file.write("\n")

#print file.read()

print "Truncating you file ..."

#file.truncate()

#print "See.. file : " + file.read()

print "Writing your file"

line = raw_input("enter a line");
file.write(line)
file.write("\n")
line = raw_input("enter another line");
file.write(line)
file.write("\n")

print 'Done!'
file.close()
