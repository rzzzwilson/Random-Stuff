k = int(input('How many times would you like to press the button?'))
s = 'A'
for i in range(k):
    if 'A' in s:
        s = s.replace('A', 'B')
        print (s)
    elif 'B' in s:
        s = s.replace('B', 'BA')
        print (s)
