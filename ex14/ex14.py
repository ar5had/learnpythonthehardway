from sys import argv

script, un, sex = argv
prompt = "=>"

print 'Hi %s, you are running %s program' % (un, script)
print 'I assume you are a good %s' % sex
print 'So tell me, do you love programming'
likes = raw_input(prompt)

print """Alright, so you said %r about liking
programming.""" % (likes)
