scores = [("Maria" , 9) , ("Ammy" , 10) , ("Alex" , 8)]

for person in scores:
    name = person[0]
    score = person[1]
    #print("Hello " + name + ". Your score is " + str(score))
    print("Hello {}. Your score is {}.".format(name , score) )

print(" ")

# user_name = input("Enter your name : ")

# print("Hello {}, Welcome!".format(user_name))


#Printing double braces:
a = 4
b = 5
print("The set of {{{} , {}}}".format(a,b)) #We need to use double braces to print out them.

x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))


#What is printed by the following statements?

s = "I saw the movie, Mary Poppins Returns, and I thought it was great."

# all the expressions
r_count = s.count("r")
all_case_r_count = s.lower().count("r")
r_precentage = all_case_r_count/len(s) * 100

# use mostly variables inside f-strings or format()
first_str = f"The number of r characters: {r_count}."
second_str = "The percentage of r characters (upper or lower case): {:.2f}%.".format(r_precentage)

# display
print( first_str + " " + second_str)