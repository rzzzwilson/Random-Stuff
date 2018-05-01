fname = 'file.txt'
file = open(fname)
filetext = file.read()
filetext = filetext.replace("\n", " ")
for word in filetext.split(" "):
    print(word)
