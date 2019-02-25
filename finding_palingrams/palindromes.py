"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

# If your file is in the same directory as the script, then you don't have to specify
# the full file path.
word_list = load_dictionary.load("words.txt")
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))

# Here, we use the splat(*) operator--the argument must be a list--to print the palindroms neatly.
# By using * in the print statement, we remove the quotations and stack the
# words in the list by seperating each word with a newline.
print(*pali_list, sep="\n")
