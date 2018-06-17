old_list = [1, 2, 3, 4, 5, 6, 7]
new_list = []
for val in old_list:
    if val % 3:
        new_list.append(val)
print(new_list)
