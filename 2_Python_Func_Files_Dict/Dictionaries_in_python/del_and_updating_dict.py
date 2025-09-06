inventory = {"apples" : 200 , "banana" : 300 , "pears" : 400 , "Grapes" : 500}
print(inventory)

# Now check initial len of inventory
print(len(inventory))

# Adding new key value pair
inventory["Mango"] = 457
print(inventory)

# Updating
inventory['apples'] = 250
print(inventory)

# Adding and Updating existing value
inventory['banana'] = inventory['banana'] + 150
print(inventory)

# Now check len of inventory
print(len(inventory))

# Creating new element from existing

inventory['orange'] = inventory["apples"]
print(inventory)

# Creating new by adding existing
inventory['watermelon'] = inventory["apples"] + inventory["orange"]
print(inventory)

# Deleting element from dict

del inventory['Mango'] # So, dictionaries are mutable.
print(inventory)