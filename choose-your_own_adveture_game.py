name = input("Enter your name: ")
print("Welcome" ,name, "to this adventure!")
round_one = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()
if round_one == "left":
    round_two = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")
    if round_two == "swim":
        print("you swam across and you were eaten by an alligator")
    elif round_two == "walk":
        print("you walked for many miles and you died hahahaaa")
    else:
        print("not a avalid option and you lose")  
elif round_one == "right":
    round_three = input( "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if round_three == "back":
        print("go back and lose")
    elif round_three == "cross":
        round_four = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if round_four == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif round_four == "No":
            print("You ignore the stranger and they are offended and you lose")
        else:
            print("not a valid option and you lose")
    else:
        print("not a valid option and you lose")
else:
    print("not a valid option and you lose")
print("thank you for playing", name)
                                

