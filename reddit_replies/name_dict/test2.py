Names = dict()

while True:
    nameinput = input("Enter a name (write 'done' if finished): ")
    if nameinput == 'done':
        break

    if nameinput not in Names:
        Names[nameinput] = 1
    else:
        Names[nameinput] += 1

print(Names)

for (name, num) in Names.items():
    print(f'{name} occurred {num} times')
