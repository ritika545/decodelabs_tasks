print("Welcome to the General Knowledge Quiz!")
print()

score = 0

# Question 1
answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer = input("\n2. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer = input("\n3. How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

print("\nQuiz Completed!")
print("Your final score is:", score, "/ 3")