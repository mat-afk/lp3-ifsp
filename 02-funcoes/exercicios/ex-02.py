numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceira número: "))

def media(*numeros):
    return sum(numeros) / len(numeros)

print(f"Média aritmética: {media(numero1, numero2, numero3)}")
