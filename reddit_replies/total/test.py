#Start of with an intro that will guide the user
def intro():
    print('This app will calculate your total points and average points per game')
    print('Enter -1 to stop entering data')

#Input the following variables that will execute the results
#Make sure to introduce the intro before making the variables otherwise it will repeat
def main():
    intro()
    #Input a variable to enter your scores
    scores = get_scores()
    #Find the total of number of scores then find the average with the total
    #Make a list in order to Input your number
    total = sum(scores)
    average = total/len(scores)
    my_list = [get_scores]
    print('you scored a total of', scores, 'points for the season')
    print('with an average of', average, 'points per game')

#Enter your following scores in which make a list and make a variable to enter score
#Include a while loop to stop the process which will enter your total score and average
def get_scores():
    game_scores = []
    while True:
        try:
            value = float(input('Enter score: '))
        except ValueError:
            pass  # Do nothing, could also print('a message')
        if value == -1:
            break
        game_scores.append(value)
    #Return your game scores 
    return game_scores


#Get your value list in which the total has to be a zero
#Make a for loop (either) to find your values
def get_total(value_list):
    total = 0.0
    for num in value_list:
        total += num
    return total



main()
