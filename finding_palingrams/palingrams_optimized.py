"""Find all word-pair palingrams in a dictionary file."""

# This script runs faster because I'm using sets to loop through the words.
# Sets are hashable via a hashtable, which allows for faster lookups.
# What took 400 seconds to run with lists now runs in 3.7 seconds with sets.
import load_dictionary

word_list = load_dictionary.load('words.txt')

# Find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:]and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()

# Sort palingrams on first word.
palingrams_sorted = sorted(palingrams)

# Display list of palingrams.
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
    