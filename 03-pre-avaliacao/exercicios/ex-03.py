frase = input("Digite uma frase para contar suas vogais e consoantes: ")

vogais = ("a", "e", "i", "o", "u")
outros = (".", ",", "/", "?", "!", "'", " ", "0", "1", "2", "3", "4", "6", "7", "8", "9")
vogais_cont = 0
consoantes_cont = 0

for letra in frase:
    if letra.lower() in vogais:
        vogais_cont += 1
    elif not letra in outros:
        consoantes_cont += 1

print(f"Vogais: {vogais_cont}")
print(f"Consoantes: {consoantes_cont}")