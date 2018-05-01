def func():
    direction = "up"

    def toggle_direction():
        nonlocal direction
        if direction == "up":
            direction = "down"
        else:
            direction = "up"
        return

    def get_direction():
         return direction

    return toggle_direction, get_direction


toggle_direction, get_direction = func()

get_direction() 
#    ->  works!

toggle_direction()    
#    -> UnboundLocalError: local variable 'direction' referenced before assignment
