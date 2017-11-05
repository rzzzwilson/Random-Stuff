n = int(input()) # N = how many input numbers
printer = [None] * n
for i in range(0, n):
    printer[i] = int(input()) # Fill the empty array
printing = False
prints = 0
top = max(printer)

i = 0
while (i < top):
    i += 1
    for num in printer:
        if (num >= i and not printing):
            prints += 1
            printing = True
        elif (num < i and printing):
            printing = False
    printing = False
print(prints)
