import random

lucky: int = random.randint(1, 100)  # lucky number

tries: int = 0
guess: int = 0
print(lucky)
while True:
    guess = int(input('Guess a number [0-100]: '))
    tries += 1

    if guess == lucky:
        break
    if guess > lucky:
        print("guess lower...")
    else:
        print("guess higher")

print(f"Correct. it took you {tries} attempts")
