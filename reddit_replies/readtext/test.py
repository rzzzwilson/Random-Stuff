with open("file.txt") as fhandle:
    for line in fhandle:
        for word in line.split():
            print(word)
