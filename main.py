import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 15
TOTAL_PROBLEMS = 5

def generate_math_problem():
    left_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS)

    math_expression = str(left_operand) + " " + operator + " " + str(right_operand)

    answer = eval(math_expression)

    return math_expression, answer

input("Press anything on keyboard to start the math challenge!")
print("#######################################################")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    math_expression, answer = generate_math_problem()

    while True:
        user_guess = input("Problem #" + str(i + 1) + ": " + math_expression + " = ")

        if user_guess == str(answer):
            break

end_time = time.time()
total_time = round(end_time -start_time, 2)

print("#######################################################")
print("Congrats!!, you completed the challenge in ", total_time, " seconds!")
