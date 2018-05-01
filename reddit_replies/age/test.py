# Calculates appropriate dating age
x = input("What's your age? ")
x = int(x)

def age_formula(my_age):
    age = my_age/2 + 7
    return age

limit = age_formula(x)
print("You can date someone", limit, "years old, or older.")
