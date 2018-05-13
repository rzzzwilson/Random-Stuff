words = []

def getWords():
    user_in = input('Enter a sentence: ').split()
    while True:
        for i in user_in:
            if i not in words:
                words.append(i)
            else:
                getWords()

        return print(words)


getWords()
