def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    while right_is_clear():
       turn_right()
       move()      
    if not right_is_clear():
       turn_left()
    