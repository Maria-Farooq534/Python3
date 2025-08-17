'''addition_str is a string with a list of numbers separated by the + sign. Write code that uses the 
accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). 
(You should use the .split("+") function to split by "+" and int() to cast to an integer).'''


# addition_str = "2+5+10+20"
# addition = addition_str.split("+")
# print(addition)
# sum_val = 0
# for item in addition:
#     int_item = int(item)
#     sum_val += int_item
# print(sum_val)


# '''week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that 
# uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to 
# avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items 
# in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).'''

# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
# week_temp_list = week_temps_f.split(",")
# sum_temp = 0
# for temp in week_temp_list:
#     float_temp = float(temp)
#     sum_temp = sum_temp + float_temp
# avg_temp = sum_temp/(len(week_temp_list))
# print(avg_temp)



# '''Write code to create a list of word lengths for the words in original_str using the accumulation pattern 
# and assign the answer to a variable num_words_list. (You should use the len function).'''

# original_str = "The quick brown rhino jumped over the extremely lazy fox"
# num_words_list = []
# original_list = original_str.split(" ")
# #print(original_list)

# for word in original_list:
#     word_length = len(word)
#     num_words_list.append(word_length)
# print(num_words_list)



#Which of these is a correct reference diagram following the execution of the following code?

# sent = "The mall has excellent sales right now."
# wrds = sent.split()
# print(wrds)
# wrds[1] = 'store'
# print(wrds)
# new_sent = " ".join(wrds)
# print(new_sent)

# # multiplying list
# list1 = [1,2,3]
# new = list1 * 2
# print(new)


#Given the list of numbers, numbs, modifiy the list numbs so that each of the original numbers 
# are increased by 5. Note this is not an accumulator pattern problem, but its a good review.

# nums = [2,5,7,8]
# for i in range(len(nums)):
#     nums[i] = nums[i] + 5
# print(nums)


# #accumulating a string
# s = input("Enter some text")
# ac = ""
# for c in s:
#     ac = ac + c + "-"

# print(ac)


# colors = ["Red", "Purple", "Yellow"]

# for position in range(len(colors) - 1):
#     color = colors[position]
#     print(color)
#     if color[0] in ["P", "B", "T"]:
#         del colors[position]

# print(colors)


# #What if we mutate a list when we iterate that list : there will be infinite loop
# colors = ["Red", "Orange", "Indigo"]

# for color in colors:
#     if color[0] in ["A", "E", "I", "O", "U"]:
#         colors.append(color)

#     print(colors)

#     if len(colors)>6: #if we have not added this break, there will be an infinite loop that never ends.
#         break



# a = ["holiday", "celebrate!"]
# b = a
# b.append("company")
# print(a)
# print(b)


# #Given that we want to accumulate the total number of strings in the list, 
# lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
# sum = 0
# for item in lst:
#     if type(item) == type("string"):
#         sum = sum + 1

# print(sum)

