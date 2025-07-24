import random

choices =  ["rock","paper","scissors"]

def decide_winner(user,computer):
    if user == computer:
        return "It's a tie!"
    elif(user == "rock" and computer == "scissors")or\
        (user == "scissors" and computer == "paper")or\
        (user == "paper" and computer == "rock"):
        return "You Win!"
    else:
        return "Computer wins!"
    
    
while True:
    user_choice = input("Enter rock, paper, or scissors  (or 'exit' to quit): ").lower()
    
    
    if user_choice == "exit":
        print("Thanks For Playing!")
        break
    
    if user_choice not in choices:
        print("Invalid Choice. Try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose : {computer_choice}")
    print(decide_winner(user_choice, computer_choice))
    
    
    
    
    
    
# #Code Explanation 👨‍💻
# Here's a breakdown of what each line in your Python script does.

# import random
# This line imports Python's built-in random module, which contains functions for generating random numbers and making random choices. You need this for the computer's move.

# choices = ["rock", "paper", "scissors"]
# This creates a list named choices. A list is a data structure that holds an ordered collection of items. This specific list holds the three valid string options for the game. It will be used to validate user input and for the computer to select its move from.

# def decide_winner(user, computer):
# This line defines a function called decide_winner. A function is a reusable block of code that performs a specific task. This one takes two arguments (inputs): user (the user's choice) and computer (the computer's choice). Its purpose is to determine the outcome of the game round.

# if user == computer:
# Inside the function, this is the first condition. It checks if the value of the user variable is exactly the same as the computer variable.

# return "It's a tie!"
# If the if condition above is true, the function stops and sends back the string "It's a tie!" as its result.

# elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
# If the first if condition was false, the code checks this elif (else if) condition. This is the main game logic for a user win. It checks all three winning combinations for the user using and and or operators. The \ at the end of the first line is just to break the long line of code into two for better readability.

# return "You Win!"
# If any of the winning combinations in the elif statement are true, the function returns the string "You Win!".

# else:
# If it's not a tie and the user didn't win, this else statement catches all remaining possibilities, which means the computer must have won.

# return "Computer wins!"
# If the else condition is met, the function returns the string "Computer wins!".

# while True:
# This line starts an infinite loop. The code inside this loop will repeat forever until it's explicitly told to stop (using a break statement). This keeps the game running for multiple rounds.

# user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
# This line does two things:

# input(...): Prompts the user with the message in the quotes and waits for them to type something and press Enter.

# .lower(): Converts whatever the user typed into all lowercase. This makes the input case-insensitive (so "Rock", "ROCK", and "rock" are all treated the same).
# The final lowercase text is stored in the user_choice variable.

# if user_choice == "exit":
# This checks if the user typed "exit".

# print("Thanks For Playing!")
# If the user typed "exit", this line prints a goodbye message.

# break
# This command immediately terminates the while loop, which ends the program.

# if user_choice not in choices:
# This validates the user's input. It checks if the user_choice is not found in the choices list you defined at the beginning. This is how you catch typos or invalid words.

# print("Invalid Choice. Try again.")
# If the input was invalid, this message is printed.

# continue
# This command stops the current iteration of the loop and immediately jumps back to the beginning of the while loop, asking for user input again. It skips the computer's turn.

# computer_choice = random.choice(choices)
# This is where the computer makes its move. random.choice(choices) picks one random item from your choices list, and the result is stored in the computer_choice variable.

# print(f"Computer chose: {computer_choice}")
# This line uses an f-string to print what the computer chose. The f before the string allows you to embed variable values directly inside curly braces {}.

# print(decide_winner(user_choice, computer_choice))
# This is the final step. It calls the decide_winner function, passing it the user's and computer's choices. The function runs, returns a result string (like "You Win!"), and the print command displays that result on the screen.
    