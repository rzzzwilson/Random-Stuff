import turtle as t

window=t.Screen()
window.bgcolor(input("Enter the background color"))
window.title(input("Enter the title"))
crimson=t.Turtle()
crimson.color(input("Enter the color of turtle"))
crimson.forward(int("Enter steps forward"))
crimson.left(90)
x=45
crimson.forward(x)
window.mainloop()
