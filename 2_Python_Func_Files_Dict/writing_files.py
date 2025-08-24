#Writing Files
file_obj = open("squares.txt" ,"w")
for num in range(13):
    square = num * num
    file_obj.write(str(square))
    file_obj.write('\n')
file_obj.close()
#print(file_obj)

#Now read that file
read_file = open("squares.txt" , 'r')
print(read_file.read())
read_file.close()