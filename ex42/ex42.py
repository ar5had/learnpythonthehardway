class Parent(object):
    def q(self):
        print "This is parent method"

class Child(Parent):
    def p(self):
        print "this is child method"

child = Child();
child.q()
child.p()
