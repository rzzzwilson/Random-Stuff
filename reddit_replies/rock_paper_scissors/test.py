# need this for randint()
import random

# generate two random numbers b/w 1-3
# each player is a random number b/w 1-3
p1 = random.randint(1,3)
p2 = random.randint(1,3)

# define variables, rock, paper, scissors
Rock = 1
Paper = 2
Scissors = 3


# 3 cases when p1 can win:

elif p1 == rock and p2 == scissors:
print("p1 wins, rock breaks scissors")

elif p1 == paper and p2 == rock:
print("p1 wins, paper covers rock")

elif p1 == scissors and p2 == paper:
print("p1 wins, scissors cut paper")

# 3 cases when p2 can win:
elif p2 == rock and p1 == scissors:
print("p2 wins, rock breaks scissors")
elif p2 == paper and p1 == rock:
print("p2 wins, paper covers rock")
elif p2 == scissors and p1 == paper:
print("p2 wins, scissors cut paper")

# 3 cases when they tie
elif p1 == rock and p2 == rock:
print("tie!")
elif p1 == paper and p2 == paper:
print("tie!")
elif p1 == scissors and p2 == scissors:
print("tie!")

