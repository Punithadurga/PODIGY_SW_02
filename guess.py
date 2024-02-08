import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Guess the Number game!")

    while not guessed_correctly:
        # Prompt user to enter a guess
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        
        # Increment attempts
        attempts += 1
        
        # Compare the user's guess with the secret number
        if user_guess == secret_number:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
   
if __name__ == "__main__":
    guess_the_number()
