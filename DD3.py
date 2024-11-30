import random

number = random.randint(1, 10)
attempts = 3

print("Вгадайте число від 1 до 10. У вас є три спроби.")
for attempt in range(attempts):
    guess = int(input("Ваш варіант: "))
    if guess > number:
        print("Менше")
    elif guess < number:
        print("Більше")
    else:
        print("Вітаємо! Ви вгадали число.")
        break
else:
    print(f"Ви програли. Загадане число було: {number}")