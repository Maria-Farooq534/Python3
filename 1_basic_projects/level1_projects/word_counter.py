"""
Word Counter

Take a sentence as input.

Count words, letters, and occurrences of each word.

(Use .split(), .count(), dictionaries later if you want).

"""

sentence = input("Enter a sentence : ")
print("Sentence you entered : ", sentence)

# Words
# Sentence List
sent_list = sentence.split()
print("There are ", len(sent_list), "words in it.")

# Characters
print(f"There are {len(sentence)} characters in it.")

char_occ = {}
# Occurance of each character
for sent in sentence:
    if sent not in char_occ:
        occ = sentence.count(sent)
        char_occ[sent] = occ
print(char_occ)



