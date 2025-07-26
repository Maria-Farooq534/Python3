# a = 5
# b = len("Hello")

# print(a+b)

# print(2 * len("hello") + len("goodbye"))
# #how python evaluates this expression
# # len(hello) is 5
# # len("goodbye") is 7
# # So, the expression becomes (2 * 5 * 7)
# # Python follows PEMDAS
# # First 2*5 = 10
# # then 10 + 7 = 17

def square(n):
    return n*n


def sub(x , y):
    return x-y
    

x= 2
y=1

print(square(y+3))
print(square(y + square(2))) # square(2) = 4 , 1+4 = 5, square(5) = 25.
print(sub(square(y) , square(x))) # square(y)= 1, square(x) = 4 , sub(1,4) = -3
