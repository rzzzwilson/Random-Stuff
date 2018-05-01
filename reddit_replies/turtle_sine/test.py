import turtle, math

def createTurtle(count):
    for x in range(count):
        turtle_dict[x] = turtle.Turtle()
        turtle_dict[x].shape("turtle")
        turtle_dict[x].color(color_list[x])
        turtle_dict[x].width(3)
        return turtle_dict[x]

def wave(count):
    for n in range(count):
        amp = amp_list[n]
        freq = freq_list[n]
        createTurtle(n)
        for x in range(361):
            y_val = amp * math.sin(math.radians(x * freq))
            turtle_dict.values().goto(x, y_val)
            print(x, y_val)

num_waves = int(input("How many sine waves do you want to create? "))
amp_list = []
freq_list = []
turtle_dict = {1 : "alpha", 2 : "beta", 3 : "gamma", 4 : "delta", 5 : "omega"}
color_list = ["red", "blue", "green", "purple", "pink"]
counter = 1

for x in range(num_waves):
    print("\nSine Wave #" , counter)
    amp = int(input("Enter the amplitude of the sine wave: "))
    freq = float(input("Enter the frequency of the sine wave: "))
    amp_list.append(amp)
    freq_list.append(freq)
    counter += 1

print(amp_list)
print(freq_list)
print(turtle_dict)

amp_screen = max(amp_list) + 1

win = turtle.Screen()
win.bgcolor("lightyellow")
win.setworldcoordinates(0,-amp_screen, 500 ,amp_screen)

wave(counter-1)

win.exitonclick()
