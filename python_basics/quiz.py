'''addition_str is a string with a list of numbers separated by the + sign. Write code that uses the 
accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). 
(You should use the .split("+") function to split by "+" and int() to cast to an integer).'''


addition_str = "2+5+10+20"
addition = addition_str.split("+")
print(addition)
sum_val = 0
for item in addition:
    int_item = int(item)
    sum_val += int_item
print(sum_val)


'''week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that 
uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to 
avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items 
in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).'''

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temp_list = week_temps_f.split(",")
sum_temp = 0
for temp in week_temp_list:
    float_temp = float(temp)
    sum_temp = sum_temp + float_temp
avg_temp = sum_temp/(len(week_temp_list))
print(avg_temp)



'''Write code to create a list of word lengths for the words in original_str using the accumulation pattern 
and assign the answer to a variable num_words_list. (You should use the len function).'''

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []
original_list = original_str.split(" ")
#print(original_list)

for word in original_list:
    word_length = len(word)
    num_words_list.append(word_length)
print(num_words_list)
