"""
Write a program that finds the key in a dictionary that has the maximum value. 
If two keys have the same maximum value, it’s OK to print out either one. 
Fill in the skeleton code
"""

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = list(d.keys())
best_key_so_far = ks[0] # initialize variable best_key_so_far to be the first key in d


for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))


"""
1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to key_with_min_value.
"""

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}
for c in placement:
    if c not in d:
        d[c] = 0
    d[c] = d[c] + 1
print(d)

keys = list(d.keys())
print(keys)
key_with_min_value = keys[0]
for key in keys:
    if d[key] < d[key_with_min_value]:
        key_with_min_value = key


"""
5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to key_with_max_value.
"""

product = "iphone and android phones"
lett_d = {}

for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] = lett_d[char] + 1
print(lett_d)

keys = list(lett_d.keys())
key_with_max_value = keys[0]

for key in keys:
    if lett_d[key] > lett_d[key_with_max_value]:
        key_with_max_value = key
print(key_with_max_value)
