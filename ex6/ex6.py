x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#place1
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
#place2
print "I said: %r." % x
#place3
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#place4
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
