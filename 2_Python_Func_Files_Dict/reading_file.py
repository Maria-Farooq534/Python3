#file_ref = open("C:\\Users\\Ali\\Desktop\\Coursera\\Python_Programming\\2_Python_Func_Files_Dict\\olympic.csv" , "r")

# .read()

#content = file_ref.read()
##print(f"Number of characters :  {len(content)} ")
# print(len(lines))
# print(lines)


# .readlines()

# lines = file_ref.readlines()
# print("".join(lines[:5]))
# for line in lines:
#     print(line.strip())


# .readline()

# line = file_ref.readline()
# print(line)


# # Close file
# file_ref.close()


"""
Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to 
the variable num_lines. Do not use the len method.
"""

emotion_file = open("C:\\Users\\Ali\\Desktop\\Coursera\\Python_Programming\\2_Python_Func_Files_Dict\\emotion_words.txt" , "r")
num_lines = 0
for line in emotion_file:
    num_lines += 1
    #print(line.strip())
print(num_lines)
emotion_file.close()