import random
random_num = random.randrange(1,101)
print("Welcom to the Guess the Number Game")
print("I'm thinking a number between 1 and 100")

attempts = 0
guessed_correctly = False

while not guessed_correctly:

    try: 
        user_guess = int(input("Enter a number to guess : "))
        attempts += 1

        if user_guess < random_num:
            print(f"{user_guess} is below the number, Try again!")
        elif user_guess > random_num:
            print(f"{user_guess} is above the number, Try again!")
        else:
            print("Congragulations! You guessed it right!")
            print(f"{random_num} was indeed the number.")
            print(f"It looks like you took {attempts} attempts to guess it right.")
            guessed_correctly = True

    except ValueError:
        print("Please enter a valid number!")

    
print("Thanks for playing!")
