import math
 
# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}
 
# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wallHeight = float(input('Enter wall height (feet): \n'))
wallWidth = float(input('Enter wall width (feet): \n'))
wallArea = wallHeight * wallWidth
print('Wall area: %.1f square feet' % wallArea)
   
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
gallonsNeeded = wallArea / 350 #amount of sq ft 1 gallon covers
print('Paint needed: %.16f gallons' % gallonsNeeded)
 
# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
cansNeeded = math.ceil(gallonsNeeded)
print('Cans needed: %d can(s)' % cansNeeded)
 
# FIXME (4): Calculate and output the total cost of paint can needed depending on color
userColor = input('\nChoose a color to paint the wall: \n')
paintCost = paintColors[userColor] * cansNeeded
print('Cost of purchasing %s paint: $%d' % (userColor, paintCost))
