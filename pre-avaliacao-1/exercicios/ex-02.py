numero = int(input("Digite um número para gerar a tabuada: "))

for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")

## tabuada = [numero * i for i in range(1, 11)]