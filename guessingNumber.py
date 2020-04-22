import random
n = input('Guess a number between 0 and 100: ')
i = random.randint(1, 100)
for k in range(100):
    if i == int(n):
        print(f"coorect{k+1}")
        break
    else:
        if i < int(n):
            print("to low")
        else:
            print("too high")
        i = int(input("guess again"))
