from sys import argv

program, fn = argv

txt = open(fn)

print "Filename : %s " % fn + "\n" + txt.read()

txt.close()

txt = open(raw_input("Another fiile..."))

print "another file -->"

print txt.read()
