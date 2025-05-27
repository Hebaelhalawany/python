import random
import re

# 1. Function to generate array of specific length with incremented integers
def generate_array(length, start):
    
    return [start + i for i in range(length)]

# 2. FizzBuzz function
def fizz_buzz(number):
   
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

# 3. String reversal function
def reverse_string(input_string):
   
    return input_string[::-1]

# 4. User input validation function
def get_user_info():
   
    # Get name
    while True:
        name = input("Please enter your name: ").strip()
        if name and not name.isdigit():
            print(f"Hello, {name}!")
            break
        else:
            print("Please enter a valid name (not empty or just numbers)")
    
    # Get email
    while True:
        email = input("Please enter your email: ").strip()
        if email:
            break
        else:
            print("Please enter a valid email (not empty)")
    
    # Validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid_email = re.match(email_pattern, email) is not None
    
    print(f"\n--- User Information ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Email is {'valid' if is_valid_email else 'invalid'}")

# 5. Longest alphabetical substring function
def longest_alphabetical_substring(s):
    
    if not s:
        return ""
    
    longest = s[0]
    current = s[0]
    
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            current += s[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = s[i]
    
    # Check the last substring
    if len(current) > len(longest):
        longest = current
    
    return longest

# 6. Number processing program
def process_numbers():
  
    total = 0
    count = 0
    
    print("Enter numbers (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a number: ").strip()
        
        if user_input.lower() == 'done':
            break
        
        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Error: Please enter a valid number or 'done' to finish")
            continue
    
    if count > 0:
        average = total / count
        print(f"\n--- Results ---")
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")
    else:
        print("No valid numbers entered.")

# 7. Hangman game
def hangman_game():
   
    # List of words
    words = ["python", "programming", "computer", "algorithm", "function", 
             "variable", "string", "integer", "boolean", "array"]
    
    # Get player name
    while True:
        player_name = input("Enter your name: ").strip()
        if player_name and not player_name.isdigit():
            break
        else:
            print("Please enter a valid name")
    
    print(f"\nWelcome to Hangman, {player_name}!")
    
    # Choose random word
    word = random.choice(words).lower()
    guessed_letters = set()
    correct_guesses = set()
    max_turns = 7
    turns_left = max_turns
    
    print(f"\nWord to guess: {' '.join(['_' if letter not in correct_guesses else letter for letter in word])}")
    print(f"Turns remaining: {turns_left}")
    
    while turns_left > 0:
        # Check if word is completely guessed
        if all(letter in correct_guesses for letter in word):
            print(f"\nCongratulations {player_name}! You guessed the word: {word}")
            return
        
        # Get user guess
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            correct_guesses.add(guess)
            print("Good guess!")
        else:
            turns_left -= 1
            print(f"Wrong guess! Turns remaining: {turns_left}")
        
        # Show current progress
        current_state = ' '.join([letter if letter in correct_guesses else '_' for letter in word])
        print(f"Word: {current_state}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    
    print(f"\nGame Over! The word was: {word}")

# Demo functions
def demo_all_functions():
   
    print("=== LAB 02 SOLUTIONS DEMO ===\n")
    
    # 1. Array generation
    print("1. Array Generation:")
    arr = generate_array(5, 10)
    print(f"generate_array(5, 10) = {arr}\n")
    
    # 2. FizzBuzz
    print("2. FizzBuzz:")
    test_numbers = [3, 5, 15, 7]
    for num in test_numbers:
        print(f"fizz_buzz({num}) = {fizz_buzz(num)}")
    print()
    
    # 3. String reversal
    print("3. String Reversal:")
    test_string = "hello world"
    print(f"reverse_string('{test_string}') = '{reverse_string(test_string)}'\n")
    
    # 5. Longest alphabetical substring
    print("5. Longest Alphabetical Substring:")
    test_string = "abdulrahman"
    result = longest_alphabetical_substring(test_string)
    print(f"Longest substring in alphabetical order in '{test_string}' is: '{result}'\n")

# Main execution
if _name_ == "_main_":
    while True:
        print("\n=== LAB 02 MENU ===")
        print("1. Demo all functions")
        print("2. User info collection (with email validation)")
        print("3. Number processing program")
        print("4. Hangman game")
        print("5. Test individual functions")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            demo_all_functions()
        elif choice == "2":
            get_user_info()
        elif choice == "3":
            process_numbers()
        elif choice == "4":
            hangman_game()
        elif choice == "5":
            print("\nIndividual Function Tests:")
            print("Array generation:", generate_array(3, 5))
            print("FizzBuzz(15):", fizz_buzz(15))
            print("Reverse 'python':", reverse_string("python"))
            print("Longest alphabetical in 'programming':", longest_alphabetical_substring("programming"))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")