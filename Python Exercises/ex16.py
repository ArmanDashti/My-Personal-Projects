# import random

# chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = int(input("Enter a number: "))
# password =  "".join(random.sample(chars, passlen))
# print(password)
import string
import random

def pw_gen(size = 8, chars = string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))