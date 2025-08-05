# split_list = "This list is going to split"
# a = split_list.split()
# print(a)


# #Join
# join_list = ("/".join(a))
# print(join_list)


#What is the type of a?
b = "My, what a lovely day"
x = b.split(',') # x = ["My" , "what a lovely day"]

z = "".join(x) # z = "Mywhat a lovely day"
y = z.split() # y = ['Mywhat' , "a" , "lovely" , "day"]
a = "".join(y) # "Mywhatalovelyday"
print(a)
print(type(a))
