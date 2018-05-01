fR = open('Pets.txt', 'r')
line = fR.readline()

while not line.startswith('(Dog:'):
    line = fR.readline()

names = line.split("'")

for name in names:
    if (name[:1] == '(' or ',' or ')'):
        names.remove(name)

print(names)
fR.close()
