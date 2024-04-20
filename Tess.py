from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while front_is_clear:
        climb_wall
        if front_not_clear:
            (Do something)
break
    
def climb_wall():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    if left_is_blocked():
        turn_left()
        turn_left()
        while front_is_clear():
            move()  
        turn_right()
        move()
        turn_right()

def turn_right():
    for i in range (3):
        turn_left()
   
if _name_ == '_main_':
    main()