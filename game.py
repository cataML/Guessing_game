import random

print("\nWelcome to Rising _Force number guessing game. ")
print()
print("\nThe program has selected a number from 1 to 10. Kindly guess the number.\n ")
def play_game():
    sec_num = random.randint(1, 10)
    attempts = 5 #number of attempts 
    count = 0 # counting the number of guesses
   
    while attempts > 0:
        try: # Error if guess is not an integer
            guess = int(input("Enter your guess here: "))
        except ValueError: # Error if guess is not an integer
            print("Invalid number! Enter the valid number. ")
            continue

        attempts -= 1 # Decrease attempts count
        count  += 1 # Increase guess count
        if guess > sec_num:
            print('Too high! Enter a lower number.')

        elif guess < sec_num:
            print("Too low! Enter a higher number. ")
    
        else:
            print(f"Congratulations! You guesed the number right in {count} atempts" )
            return

        if attempts == 0:
            print(f"You are out of attempts. The correct number was {sec_num} ")
    restart = input("Do you want to play again? (yes/no): ").strip()
    if restart == "yes":
        play_game()
    else:
        print("Thank you for playing")
        return


       
play_game() #call the function to start the game       
