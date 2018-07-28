def reverse_string(str):
    str_list = str.split(" ")
    rev_str_list = str_list[::-1]
    rev_str = " ".join(rev_str_list)
    return rev_str
sentence = input("Enter A Sentence: ")
print(reverse_string(sentence))