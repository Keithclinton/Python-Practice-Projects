import random
import time
Operators = ["+", "-", "*"]
Min_Operand = 1
Max_Operand = 99
Total_problems = 15
def generate_problem():
    left = random.randint(Min_Operand, Max_Operand)
    right = random.randint(Min_Operand, Max_Operand)
    Operator = random.choice(Operators)
    expr = str(left) + " " + Operator + " " + str(right)
    answer = eval(expr)
    return expr,answer
wrong = 0
input("press any key to start")
print(".......................")
start_time = time.time()
for i in range(Total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = round(end_time - start_time, 2)
print(".......................")
print("Nice work! You Finished in ", total_time, "second")

         