s = '''
x = 5
y = [x for i in range(3)]
'''

exec(s, namespace)
print('x=%s, y=%s' % (str(x), str(y)))

exec(s, {}, {})
print('x=%s, y=%s' % (str(x), str(y)))
