import random
import time

print("\nWelcome to Rising _Force number guessing game. ")
print("\nThe program has selected a number from 1 to 10. Kindly guess the number.\n ")

def play_game():
    print("Choose difficulty level: ")
    print("\n1️ - Easy(6 attempts)")
    print("\n2 - Medium(5 attempts)")
    print("\n3 - Hard(3 attempts)" )
    
    while True:
        difficulty = int(input("Choose your level (1/2/3): "))
        if difficulty == 1:
            attempts = 6
            break
        elif difficulty == 2:
            attempts = 5
            break
        elif difficulty == 3:
            attempts = 3
            break
        else:
            print("Invalid choice, enter 1, 2 or 3.")
            print(f"You have selected level {difficulty}")
   
    while True:
        sec_num = random.randint(1, 10)
        count = 0 # counting the number of guesses
        
        start_time = time.time()
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
                end_time = time.time()  # End timer
                elapsed_time = end_time - start_time 
                print(f"Congratulations! You guesed the number right in {count} attempts" )
                print(f"Time taken: {elapsed_time:.2f} seconds.") 
                return
        
            if attempts == 0:
                end_time = time.time()
                print(f"You are out of attempts. The correct number was {sec_num} ")
        restart = input("Do you want to play again? (yes/no): ")
        if restart == "yes":
            play_game()
        else:
            print("Thank you for playing")
     
play_game() #call the function to start the game       
