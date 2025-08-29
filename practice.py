# add_data = [
    
#     (9, 'Diana Prince',18,'A','History', 95),
#     (10,'Ethan Hunt',17,'C','Math',78),
#     (11, "Maria", 23 , 'A', 'ML' , 95)
# ]

# file1 = open("student_dataset.csv" , "w")
# for data in range(add_data):
#     for i in data:
#         file1.write(str(i))    
#     file1.write("\n")
# print(file1)

import csv

# Your data to add
add_data = [
    (9, 'Diana Prince', 18, 'A', 'History', 95),
    (10, 'Ethan Hunt', 17, 'C', 'Math', 78),
    (11, "Maria", 23, 'A', 'ML', 95)
]

# First, let's create the initial dataset with headers
header = ['id', 'name', 'age', 'grade', 'subject', 'score']
initial_data = [
    [1, 'Alice Johnson', 18, 'A', 'Math', 92],
    [2, 'Bob Smith', 17, 'B', 'Science', 85],
    [3, 'Charlie Brown', 16, 'A', 'English', 88]
]

# Create and write to the CSV file
with open("student_dataset.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(header)
    
    # Write initial data
    writer.writerows(initial_data)
    
    # Write additional data
    writer.writerows(add_data)

print("CSV file created successfully!")

# Read and display the file content to verify
with open("student_dataset.csv", "r") as file:
    content = file.read()
    print("\nFile content:")
    print(content)