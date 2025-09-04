# file = open("olympic.csv" , "r")
# lines = file.readlines()
# print(lines[:5])

# print(" ")
# # Header
# header = lines[0].strip().split(",")
# print(header)

# # Values

# for row in lines[1:]:
#     values = row.strip().split()
#     if values[5] != "NA":
#         print("{} {} {}".format(values[0] , values[4], values[5]))



fileconnection = open("olympic.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}, {}, {}".format(
                vals[0],
                vals[4],
                vals[5]))
