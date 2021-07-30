import random
import re

words = ["abandoned", "multiply", "smiling", "day", "example", "rescue", "brawny", "righteous", "marvelous", "scribble", "homely"]
tries = 0
max = 10
word = random.choice(words)
chars = []

while max > 0:
    guess = input("\nEnter an alphabet: ")
    if guess in chars:
        print("You already guessed that alphabet! Try the other!")
        continue
    while True:
        if len(guess) == 1 and re.match("^[a-z]*$", guess):
            for char in word:
                if guess == char:
                    guessed = chars.append(guess)
                    print(char)
                elif char in chars:
                    print(char)
                else:
                    print("-")
            if sorted([*word]) == sorted(chars):
                print("\nYou win in " + str(tries + 1) + " tries!")
                quit()
            tries += 1
            max -= 1
            print("You already guessed", tries, "times,", max, "remaining.")
            break
        else:
            print("Enter a valid alphabet!")
            break
print("\nYou lose!")
quit()