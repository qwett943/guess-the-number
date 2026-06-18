import random
import time


def default_game():
        secret = random.randint(1, 100)
        print("Угадай число от", 1, "до", 100)
        time.sleep(0.5)
        tries = 0
        while True:
                try:
                    guess = int(input("Твой вариант: "))
                except ValueError:
                    print("Введи число, а не буквы!")
                    continue
                tries += 1
                if guess < secret:
                    time.sleep(0.5)
                    print("Больше")
                elif guess > secret:
                    time.sleep(0.5)
                    print("Меньше")
                else:
                    if tries == 1:
                        time.sleep(0.5)
                        print(f"Угадал с первой попытки!  Это {secret}. Попыток: {tries}")
                        break
                    else:
                        time.sleep(0.5)
                    print(f"Угадал! Это {secret}. Попыток: {tries}")
                    time.sleep(3)
                    break

print("Выберите режим игры: ")
time.sleep(0.5)
print("1. От 1 до 100 | 2. От x до y ")
time.sleep(0.5)
a: int = int(input("Введите 1/2: "))
if a == 1:
        default_game()
elif a == 2:
    while True:
        x = int(input("От какого числа?: "))
        time.sleep(0.5)
        y = int(input("До какого числа?: "))
        time.sleep(0.5)
        if x < y:
            break
        else:
            print("Введи числа правильно!")
            time.sleep(2)

    secret = random.randint(x, y)
    time.sleep(0.5)
    print("Угадай число от", x, "до", y)
    tries = 0
    while True:
        try:
            guess = int(input("Твой вариант: "))
        except ValueError:
            print("Введи число, а не буквы!")
            continue
        tries += 1
        if guess < secret:
            time.sleep(0.5)
            print("Больше")
        elif guess > secret:
            time.sleep(0.5)
            print("Меньше")
        else:
             if tries == 1:
                time.sleep(0.5)
                print(f"Угадал с первой попытки!  Это {secret}. Попыток: {tries}")
                break
             else:
                time.sleep(0.5)
                print(f"Угадал! Это {secret}. Попыток: {tries}")
                time.sleep(3)
                break
else:
    time.sleep(0.5)
    print("Введи 1/2!")
    time.sleep(3)
