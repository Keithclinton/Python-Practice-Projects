import random
Operators = ["+", "-", "*"]
Min_Operand = 1
Max_Operand = 1000
Total_problems = 15
def generate_problem():
    left = random.randint(Min_Operand, Max_Operand)
    right = random.randint(Min_Operand, Max_Operand)
    Operators = random.choice(Operators)
    expr = str(left) + " " + Operators + " " + str(right)
    answer = eval(expr)
    return expr,answer
for i in range(Total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break