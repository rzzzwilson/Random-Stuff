"""
Original code for the OP.
"""

passed_list = a_list
count = 0
while count <= (len(passed_list) - 2):
    check = passed_list[count] + passed_list[count + 1] + passed_list[count + 2]
    if check == (passed_list[count] * 3):
        passed_list.pop(count)
        passed_list.pop(count + 1)
        passed_list.pop(count + 2)
    count += 1

print(passed_list)
