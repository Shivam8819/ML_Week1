import random
number = random.randint(1, 100)

for i in range(5):
    guess = input("Guess the number (1-100): ")
    
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)

    if guess == number:
        print("Correct! You win!")
        break
    else:
        print("Wrong guess!")
else:
    print("Sorry!! better luck next time", number)
