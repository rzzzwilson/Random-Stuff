import math
def main():
    f = getFile()
    contents = getData(f)
    average = calculateMean(contents)
    stanDev = calculateSD(contents)
    titles = displayTitles()
    print (titles)
 
def getFile():
    openFilename = str(input("File to open: "))
 
    readFile = open(openFilename, 'r')
    return readFile
 
    readFile.close()
 
 
def getData(contents):
    f = getFile()
    contents = f.read().splitlines()
    return contents
 
def calculateMean(values):
 
    length = len(values)
 
    total_sum = 0
 
    for i in range(length):
 
        total_sum += float(values[i])
 
    average = float(total_sum*1.0 / length)
 
    return average
 
def calculateSD(values):
    print("values='%s'" % values)
 
    length = len(values)
    m = calculateMean(values)
    total_sum = 0
    for i in range(length):
        print("values[i]='%s'" % values[i])
        total_sum += float(values[i]- m)**2
    radicand = total_sum*1.0 / (length - 1)
 
    return math.sqrt(radicand)
 
def displayTitles():
    f = getFile()
    c = getData()
    num = len(f)
    print ("Number of grades: ", num)
 
main()
