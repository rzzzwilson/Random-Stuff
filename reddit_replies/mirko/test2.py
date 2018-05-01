k = int(input("How many times would you like to press the button? "))
s = "A"

for _ in range(k):
    new_s = ""
    for ch in s:
        if ch == 'A':
            new_s += 'B'
        elif ch == 'B':
            new_s += 'BA'
    s = new_s
    print(s)

a_count = 0
for ch in s:
    if ch == 'A':
        a_count += 1
print(f'A={a_count}, B={len(s)-a_count}')
