import random

def choose_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy   (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard   (5 attempts)")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    max_attempts = choose_difficulty()
    number_to_guess = random.randint(1, 100)
    attempts_used = 0

    while attempts_used < max_attempts:
        print(f"\nAttempts left: {max_attempts - attempts_used}")
        guess = get_user_guess()
        attempts_used += 1

        if guess < number_to_guess:
            print("🔻 Too low! Try again.")
        elif guess > number_to_guess:
            print("🔺 Too high! Try again.")
        else:
            print(f"\n🎉 Correct! You guessed the number in {attempts_used} attempts.")
            break
    else:
        print(f"\n💥 You've used all {max_attempts} attempts! The number was {number_to_guess}.")

def number_guessing_game():
    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    number_guessing_game()
