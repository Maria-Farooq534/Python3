"""
Simple Password Strength Checker
Input a password.
Check if it has numbers, letters, length > 8, etc.
Give feedback.
"""
user_password = input("Enter your password : ")

while True:
    if len(user_password) >= 8:
        print(f'{user_password} has {len(user_password)} characters.')
    else:
        print(f"Please enter at least 8 character password.")
    
    # numbers
    numbers = [0,1,2,3,4,5,6,7,8,9]
    if numbers in user_password:
        print(f"Password has numbers.")
    else:
        print(f"Please include numbers.")

