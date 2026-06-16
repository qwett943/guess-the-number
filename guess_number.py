import random

x = int(input("От какого числа?: "))
y = int(input("До какого числа?: "))
secret = random.randint(x, y)
print("Угадай число от", x, "до", y)
tries = 0


while True:
    guess = int(input("Твой вариант: "))
    tries += 1
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        if tries == 1:
            print(f"Угадал с первой попытки!  Это {secret}. Попыток: {tries}")
            break
        else:
            print(f"Угадал! Это {secret}. Попыток: {tries}")
            break
