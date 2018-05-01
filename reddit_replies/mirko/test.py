k = int(input("How many times would you like to press the button?"))
str = "A"
for i in range(k):
    if "A" in str:
        str = str.replace(str,"B")
        print (str)
    elif "B" in str:
        str = str.replace(str, "BA")
        print (str)
