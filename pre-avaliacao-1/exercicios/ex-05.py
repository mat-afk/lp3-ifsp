palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
print("É um palíndromo") if palavra == palavra[::-1] else print("Não é um palíndromo")