def print_two(*argss):
    arg1, arg2 = argss
    print 'arg1: %r, arg2: %r' % (arg1, arg2)

def print_two_again(arg1, arg2):
    print 'arg1: %r, arg2: %r' % (arg1, arg2)

def print_one(arg):
    print 'arg1: %r' % arg

def print_none():
    print 'I aint print anythin..'

print_two("asd", "khan")
print_two_again("asd", "khan")
print_one("asd")
print_none()
