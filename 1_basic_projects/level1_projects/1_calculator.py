"""
Calculator
Input two numbers and an operator (+, -, *, /).
Print the result.
(Use conditionals and input handling).
"""

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
operator = input("Choose an operation [ + , - , * , /] : ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2
print("The result of {} {} {} = {}.".format(num1 , operator , num2 , result))


# End of Method 1


print("\nNow using Method 2: \n")

#By using method 2 : Getting numbers from user at once

nums = input("Enter two numbers seperated by a comma : ")
num_list = nums.split(',')
# print(num_list)
# print(type(num_list))
operator_2 = input("Choose an operation [ + , - , * , /] : ")
numb1 , numb2 = map(int,num_list) # map will apply the function to each element of sequence. will make it integer and will directly assign values to numb1 and numb2.

if operator_2 == "+":
    result = numb1 + numb2
elif operator_2 == "-":
    result = numb1 - numb2
elif operator_2 == "*":
    result = numb1 * numb2
else:
    result = numb1 / numb2
print("The result of {} {} {} = {}.".format(numb1 , operator_2 , numb2 , result))

#Method 2 ends.