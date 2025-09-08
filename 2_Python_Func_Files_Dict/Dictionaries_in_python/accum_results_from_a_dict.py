file1 = open("C:\\Users\\Ali\\Desktop\\Coursera\\Python_Programming\\2_Python_Func_Files_Dict\\Dictionaries_in_python\\emotion_words.txt" , "r")
txt = file1.read()

letter_counts = {}

for letter in txt:
    if letter not in letter_counts:
        letter_counts[letter] = 0
    letter_counts[letter] = letter_counts[letter] + 1
print(letter_counts)

# letter values based on their occurance
letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}
print(letter_values)

# To compute the total score of the file

scrabble_scores = 0

for letter in letter_counts:
    if letter in letter_values:
        scrabble_scores = scrabble_scores + letter_values[letter] * letter_counts[letter]
print(f"Total Scrabble Score : {scrabble_scores}")