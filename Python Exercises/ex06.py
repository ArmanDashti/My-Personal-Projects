word = input("Enter A Word: ")
check = True
for i in range(len(word)):
    if word[i] != word[len(word)-i-1]:
        check = False
        break
if check:
    print("{} is a palindrome.".format(word))
else:
    print("{} isn't a palindrome.".format(word))