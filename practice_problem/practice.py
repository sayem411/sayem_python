import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
running = True     

print("NUMBER GUESSING GAME")
print(f"Guess number between {lowest_num} to {highest_num}")

while running:
    guess = input("Enter a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Number is out of range!")
        elif guess < answer:
            print("Too low!! Try again")
        elif guess > answer:
            print("Too high!! Try again")
        elif guess == answer:
            print(f"CORRECT!! The answer was {answer}")
            print(f"Number of guesses needed: {guesses}")
            running = False   
    else:
        print("Invalid input! Enter a number only")