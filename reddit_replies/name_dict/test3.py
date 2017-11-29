from collections import defaultdict

Names = defaultdict(int)

while True:
    nameinput = input("Enter a name (write 'done' if finished): ")
    if nameinput == 'done':
        break

    Names[nameinput] += 1

print(Names)

for (name, num) in Names.items():
    print(f'{name} occurred {num} times')
