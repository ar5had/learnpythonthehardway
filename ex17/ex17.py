from sys import argv
from os.path import exists

fn, frm, to = argv

print "Copying from %s to %s" % (frm, to)

data = open(frm).read()

print 'Source file is %d bits long' % len(data)

dest = open(to, 'w')
dest.write(data)

print 'All things done!'

dest.close()
