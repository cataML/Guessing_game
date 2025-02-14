import random
sec_num = random.randint(1, 10)
attempts = 5
count = 0

print("\nWelcome to Rising _Force number guessing game. ")
print("\nThe program has selected a number from 1 to 10. Kindly guess the number.\n ")
def guess():
    global attempts
    global count
    while attempts > 0:
        try:
            guess = int(input("Enter your guess here: "))
        except ValueError:
            print("Invalid number! Enter the valid number. ")
            continue

        attempts -= 1
        count  += 1
        if guess > sec_num:
            print('Too high! Enter a lower number.')

        elif guess < sec_num:
            print("Too low! Enter a higher number. ")
    
        else:
            print(f"Congratulations! You guesed the number right in {count} atempts" )
            return

        if attempts == 0:
            print(f"You are out of attempts. The correct number was {sec_num} ")
            print("Game over")

        if guess >10:
            print("Out of rannge. Guess anumber from 1 to 10")
guess()        
