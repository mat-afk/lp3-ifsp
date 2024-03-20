import random

secret = random.randint(1, 100)
print(secret)

while True:
    guess = int(input("Digite um palpite para o número secreto de 1 a 100: "))

    if guess > secret:
        print("Palpite alto.")
    elif guess < secret:
        print("Palpite baixo.")
    else:
        print("Número correto! =)")
        break
