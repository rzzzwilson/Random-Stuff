from sys import argv

print(argv)
script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you know where you are %s?" % user_name
where = raw_input(prompt)

print "No, you're in my dream, %s?" % user_name
dream = raw_input(prompt)

print """
You are in a %r. That's right.
But you're in my dream, %r.
""" % (where, dream)

from sys import argv

script, Dream, Dolores = argv
prompt = '> '

print "Welcome %s to my %s." % (Dolores, Dream)
print "Analysis."
print "What are you feeling %s?" % Dolores
feeling = raw_input(prompt)

print "Why are you feeling that, %s" % Dolores
that = raw_input(prompt)

print """
So you're feeling %r. That's understandableself.
Why? %r.
But that's not true. Dreams are everything.
""" % (feeling, that)
