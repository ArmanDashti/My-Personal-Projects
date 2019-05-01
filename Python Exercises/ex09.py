import random
num = random.randint(1,9)
guess = 0
while True:
    guess = int(input("Enter A Number: "))
    if guess == num:
        print("You have entered the right number.")
        break
    elif guess > num:
        print("Guess a lower number.")
        continue
    else:
        print("Guess a higher number.")
        continue