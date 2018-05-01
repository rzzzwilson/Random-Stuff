import turtle 
 
 
def draw_square(some_turtle, sequence): 
    #for i in range(0, len(sequence)): 
    for (i, x) in enumerate(sequence): 
        x = x//10
        if i < 2: 
            for j in range(1, 5): 
                #some_turtle.forward(sequence[i]) 
                some_turtle.forward(x) 
                some_turtle.right(90) 
            #some_turtle.forward(sequence[i]) 
            some_turtle.forward(x) 
            if i == 1: 
                some_turtle.left(90) 
        else: 
            for k in range(1, 6): 
                #some_turtle.forward(sequence[i]) 
                some_turtle.forward(x) 
                some_turtle.left(90) 
            #some_turtle.forward(sequence[i]) 
            some_turtle.forward(x) 
 
 
def fib(n): 
    result = [] 
    a = 1 
    b = 1 
    while a < n: 
        result.append(a) 
        #tmp_var = b 
        #b += a 
        #a = tmp_var 
        b, a = b+a, b
    return result 
 
 
def draw_sequence(n, speed): 
    window = turtle.Screen() 
    window.bgcolor('white') 
    window.screensize(n**1.2, n**1.2) 

    alpha = turtle.Turtle() 
    alpha.shape('classic') 
    alpha.color('black') 
    alpha.speed(speed) 
 
    draw_square(alpha, fib(n)) 
    # draw_circle(alpha, fib(n)) 
 
    #turtle.getscreen().getcanvas().postscript(file='screen.eps')
    turtle.getscreen().getcanvas().postscript(file='screen.eps')

    window.exitonclick() 
 
 
draw_sequence(2500, 0) 
