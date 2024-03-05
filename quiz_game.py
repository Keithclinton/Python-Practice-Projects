print("Welcome to my quiz game")
playing = input("Do you want to play:")
if playing.lower() != "yes":
    quit()
print("Okay,Lets play!")  
score = 0

Answer = input("What does RAM stand for? ")
if Answer == "Random Access Memory":
    print("Correct")
    score += 1
else:
    print("Try again")

Answer = input("What does GPU stand for ")
if Answer == "Graphical Processing Unit":
    print("Correct")
    score += 1
else:
    print("Try again")

 

Answer = input("What does CPU stand for? ")
if Answer == "Central Processing Unit":
    print("Correct")
    score += 1    
else:
    print("Try again")
print("You got " + str(score) + " Questions correct")
print("You got " + str((score/4)*100) + "%.")
