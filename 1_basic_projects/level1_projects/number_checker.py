"""
Odd/Even & Prime Number Checker

Take a number and check if it’s odd/even.

Extend it to check if it’s prime.
"""

number = int(input("Enter a number : "))

if number % 2 == 0:
    print(f"The {number} is even.")
else:
    print(f"The {number} is odd.")

# Checking if a number is prime number 

if number <= 1:
    print(f"The number {number} is not a prime number.")
else:
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number, It is divisible by {num}")


"""
it means, when we do this , (2, 5) , let say 5 a number enter by user, so we write that number in for 
loop and as starting from 2 , it check 5 % 2 != 0 , false, move next 5%3 != 0 , move next 5%4 != 0 , 
next, we know 5%5 == 0 , true , so we have to iterate that number from range of 2 or whatever range we will specifiy, 
to that number and then we will check that is this number is perfectly divisible only to itself or is there 
any number comes before that number that when divided by that number , gives remainder of 0?

when we have to check 5 , we will set range (2, 5) this check the number from range of 2 to 4, as n = 5 and 
range checks from 2 to n-1 , 2 to 4. no need to check the number by number itself , as we already know that
number % number = 0 , 5 % 5 = 0.
"""