from sys import argv

pn, fn = argv

def printAll(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(lc, f):
    print lc, f.readline()

cf = open(fn)

print 'LLets do some stuff!!!'

printAll(cf)

print 'rewinding....'

rewind(cf)

print 'Printing first three lines of file'

cl = 1
print_a_line(cl, cf)

cl += 1
print_a_line(cl, cf)

cl += 1
print_a_line(cl, cf)
