file1 = open("C:\\Users\\Ali\\Desktop\\Coursera\\Python_Programming\\2_Python_Func_Files_Dict\\Dictionaries_in_python\\emotion_words.txt" , "r")
# file1 = open("emotion_wprds.txt" , 'r')
txt = file1.read()

count_t = 0
for char in txt:
    if char == "t":
        count_t += 1
print(count_t)

# Accumulating multiple variables 

x = {} # start with empty dict
x['t'] = 0
x['r'] = 0

print(x) # Now we have assigned t and r as the keys of "x" dictionary.
# Hardcoding

# for char in txt:
#     if char == 't':
#         x['t'] = x['t'] + 1
#     elif char == 'r':
#         x['r'] = x['r'] + 1


# Instead of this hard coding, we can do this as :

for char in txt:
    if char == 't':
        x[char] = x[char] + 1
    elif char == 'r':
        x[char] = x[char] + 1

print(x)
print(f"r has {x['r']} occurances")
print(f"t has {x['t']} occurances")

print(" ")

# What if we want to store each chacter in the txt to the dictionay: 
y = {}
for char in txt:
    if char not in y:
        y[char] = 0
    y[char] = y[char] + 1

print(f"a : {y["a"]} occurances")
print(f"b: {y["b"]} occurances")
print(f"r : {x['r']} occurances")
print(f"t : {x['t']} occurances")
print(y)



f = open("C:\\Users\\Ali\\Desktop\\Coursera\\Python_Programming\\2_Python_Func_Files_Dict\\Dictionaries_in_python\\emotion_words.txt" , "r")

txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

# Write a loop that prints the letters and their counts
letter_list = list(letter_counts.items())
print(letter_list)
for letter in letter_list:
    m,n = letter
    print(f"{m} : {n}")
    #print(f"{letter[0]} : {letter_list(letter[1])} occurances ")
