fruits = {"apples" : 200 , "banana" : 300 , "pears" : 400 , "Grapes" : 500}
alias = fruits 

print(f"id of fruits  is : {id(fruits)} and alias is : {id(alias)}")

print(fruits is alias) # True

alias['banana']  = 600 # its going to change fruits as well. bcz both fruits and alias are alias to each other, referencing same object.
print(fruits)

# What if we dont want to change the original
inventory = {"apples" : 200 , "banana" : 300 , "pears" : 400 , "Grapes" : 500}
alias_2 = inventory
inventory_copy = inventory.copy()
alias_2['cherry'] = 120
print(alias_2)
print(inventory)
print(inventory_copy)