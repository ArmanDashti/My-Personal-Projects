import random
def cow_bull(num):
	user_num = input("Enter a Number: ")
	counter = 1
	cows = 0
	bulls = 0
	num = str(num)
	if user_num == num:
		print("You have guessed the right number after {} tries.".format(counter))
	while num != user_num:
		for i in range(4):
			if user_num[i] in num:
				if user_num[i] == num[i]:
					cows += 1
					continue
				bulls += 1
		print("{} cows, {} bulls".format(cows,bulls))
		counter += 1
		user_num = input("Enter a Number: ")
		if user_num == num:
			print("You have guessed the right number after {} tries.".format(counter))
		cows = 0
		bulls = 0
if __name__ == "__main__":
	randomNumber = random.randint(1000,9999)
	print(randomNumber)
	cow_bull(randomNumber)