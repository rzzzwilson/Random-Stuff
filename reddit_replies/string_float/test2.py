import math

def main():
    """Some explanation of what you are trying to do."""

    filename = input('File to open: ')
    contents = getData(filename)
    print('contents=%s' % contents)
    mean = calculateMean(contents)
    print('mean=%f' % mean)
    std_dev = calculateSD(contents, mean)
    print('std_dev=%f' % std_dev)
    displayTitles(contents)
 
def getData(filename):
    """Get a list of float values from the given file."""

    with open(filename, 'r') as f:
        lines = f.readlines()
        return [float(x) for x in lines]

    # or this, if you don't understand the 'with'
#    f = open(filename, 'r')
#    contents = [float(x) for x in f.readlines()]
#    f.close()
#    return contents
 
def calculateMean(values):
    """Calculate the mean of a list of float values."""

    return sum(values)/len(values)
 
def calculateSD(values, mean):
    """Calculate the standard deviation from 'values' and the 'mean'."""

    num_values = len(values)
    total_sum = sum((i - mean)**2 for i in values)
    radicand = total_sum / (num_values - 1)
    return math.sqrt(radicand)

    # or this
#    num_values = len(values)
#    total_sum = 0
#    for i in values:
#        total_sum += (i - mean)**2
#    radicand = total_sum / (num_values - 1)
#    return math.sqrt(radicand)
 
def displayTitles(values):
    """More to come here?"""

    print ("Number of grades: ", len(values))
 
main()
