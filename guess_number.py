import random

secret = random.randint(1, 100)
print("Угадай число от 1 до 100")
tries = 0

while True:
    guess = int(input("Твой вариант: "))
    tries += 1
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print(f"Угадал! Это {secret}. Попыток: {tries}")
        break
