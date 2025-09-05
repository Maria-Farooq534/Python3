fruits = {'apples': 250, 'banana': 450, 'pears': 400, 'Grapes': 500, 'Mango': 457, 'orange': 250, 'watermelon': 500}
print(len(fruits))

# Accessing Keys
keys = fruits.keys()
print(keys)

# Accessing Values
values = fruits.values()
print(values)

# Iterating over keys:
for key in fruits.keys():
    print(key)

# Accessing both key and values
for key in fruits.keys():
    print(key, "has value ", fruits[key])


# Creating a list of keys
fruits_keys = list(fruits.keys()) # It creates a list but there is no order of elements, how they will appear
print(fruits_keys)


fruits_values = list(fruits.values())
print(fruits_values)

# Dict as a list of tuples
fruits_list = list(fruits.items())
print(fruits_list)

for key in fruits:
    print(f"Got {key} that maps {fruits[key]}")

# Check conditions

print("banana" in fruits) # True
print("mango" in fruits) # False
print("Mango" not in fruits) # False
print("Mango" in fruits) # True

if "banana" in fruits:
    print('We have' , fruits['banana'] , 'bananas')
else:
    print("We have no banana.")


# .get Method

print(fruits.get('banana')) # This will be same as fruits['banana']. (fruits sub banana)

# .get method with the object that does not exist in dict
print(fruits.get('cherry')) # returns None
# we can do same thing as:
# print(fruits['cherry']) 
# But it gives KeyError

# .get has optional parameter 
# This tells that if there is no key with this name, then create a key and assign it the given value

print(fruits.get('cherry' , 0))
print(fruits) # But still the original dict is same


# If we have cherry
fruits = {'apples': 250, 'banana': 450, 'cherry' : 330 , 'pears': 400, 'Grapes': 500, 'Mango': 457, 'orange': 250, 'watermelon': 500}
print(fruits.get('cherry' , 23)) # This time, optional parameter is not going to be used.
