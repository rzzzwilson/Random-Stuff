s = 'anaghjshb sbgdfbsnshssghstjsjyyasabcdefggreageragaergareg' #test case that can be changed
list1 = [] #this is a list for the value of how many times in order the different sections of the string appear
list2 = []
#this is a list for the position of when that happens. I.E what placement corresponds to the above values.
counter =  0
for x in range(len(s)-1):
    if int(ord(s[x])) <= int(ord(s[x + 1])):
        counter += 1
    else:
        list1.append(counter+1);#designated for reddit
        list2.append(x-counter);
        counter = 0
list1.append(counter+1);
list2.append(x-counter+1);
counter = 0
compare1 = max(list1)
compare2 = list1.index(compare1)
compare2 = list2[compare2]
print("Longest substring in alphabetical order is: " +    s[compare2:compare2 + compare1])
