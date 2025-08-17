# #Given that we want to accumulate the total number of strings in the list
# lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
# sum1 = 0
# for item in lst:
#     if type(item) == type("string"):
#         sum1 = sum1 + 1

# print(sum1)

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

