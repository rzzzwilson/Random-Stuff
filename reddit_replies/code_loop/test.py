keeptrying = True              #Defaults keeptrying to be true

def numselect():               #Defines numselecet function

    num = input("Enter an number: ")   #sets variable num to user input

    def is_int():                   #Sets is_int to be True if num is an integer, false otherwise
        if (type(num) == int):
            is_int() == True
        else:
            is_int == False

        return is_int(num)          #Returns t/f value of is_int() for user inputted 'num'

        if is_int(num) == True:                      #If user input 'num' is an integer,
            keeptrying == False                      #makes keep trying false so the program does not run again
            print ("Your number is an interger")     #and tells the usery they chose an integer

        elif is_int(num) == False:                             #If user input 'num' is not an integer.
            print ("You have not selected an integer.")   #makes keeptrying true so numselect() function will run again,
            keeptrying == True                                 #and tells the user they have not chosen an integer

while keeptrying == True:            #Continues running numselect funtion while keeptrying is still True
    numselect()
