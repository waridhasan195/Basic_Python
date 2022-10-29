
import random
randomeNumberRange = input("Input a Randome Number Range : ")

if randomeNumberRange.isdigit():
    randomeNumberRange = int(randomeNumberRange)
    if randomeNumberRange <= 0:
        print("Please type grater theen 0 range")
        quit()
    
else:
    print("Please type Numeric Digits for input.")

randomeNumber = random.randint(0, randomeNumberRange)
guess = 0


while True:
    guess += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Please type Numeric Digits for Guess.")
        continue

    if user_guess == randomeNumber:
        print("You Got It.")
        break

    elif user_guess > randomeNumber:
        print("You You were above the number!")

    elif user_guess < randomeNumber:
        print("You You were below the number!")
    
print("You got it in", guess, "guesses")
    



