import random
import time

print("Выберите режим игры: ")
time.sleep(0.5)
print("1. От 1 до 100 | 2. От x до y ")
time.sleep(0.5)
a: int = int(input("Введите 1/2: "))

def mode3():
    if a != 1 and a != 2:
        time.sleep(1)
        print("are you serious? :)")
mode3()

def mode1():
    if a == 2:
        x = int(input("От какого числа?: "))
        time.sleep(0.5)
        y = int(input("До какого числа?: "))
        time.sleep(0.5)
        secret = random.randint(x, y)
        time.sleep(0.5)
        print("Угадай число от", x, "до", y)
        tries = 0

        while True:
            guess = int(input("Твой вариант: "))
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
                break
mode1()

def mode2():
    if a == 1:
        secret = random.randint(1, 100)
        print("Угадай число от", 1, "до", 100)
        tries = 0
        while   True:
            guess = int(input("Твой вариант: "))
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
                break
