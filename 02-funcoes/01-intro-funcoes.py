# Função
# modularizar o programa
# reuso
# manutenabilidade (correção de erros e novas funcionalidades)

# declaração

def hello_world():
    print("Hello, world")

# chamada
hello_world()
hello_world()

# função sem retorno
# side effect

def imprimir_mensagem(nome):
    print(f"Bom dia, {nome}")

imprimir_mensagem("Latorre")

# função com retorno
# função pura

def mensagem(nome):
    return f"Bom dia, {nome}"

print(mensagem("Latorre"))

# parâmetros e argumentos

def somar(n1, n2):
    return n1 + n2

numero = 5

print(somar(3, 4))
print(somar(7.0, numero))
print(somar(10, somar(2, 3)))

# escopo de variáveis

def media(nota1, nota2, nota3):
    resultado = nota1 + nota2 + nota3 / 3
    return resultado

# print(resultado)

# parâmetros com valor padrão

def mensagem(nome, mensagem = "Bom dia"):
    return f"{mensagem}, {nome}."

mensagem("Quirino", "Boa noite")
mensagem("Quirino")

# argumentos nomeados

print("Olá", "123", "teste", sep="@", end="\n\n\n")
print("TESTE")

mensagem(mensagem="Boooooooooa tarde", nome="Domingos")

# docstring

def somar(n1, n2):
    '''
    Função que soma dois números

    :param n1: primeiro número
    :param n2: segundo número
    :return: soma dos números
    '''
    return n1 + n2

somar(1, 5)

# funções built-in
# print, type, min, max, int, str, bool, float, len, sum

def media(*notas):
    return sum(notas) / len(notas)

print(media(10, 40, 50))
print(media(10, 40, 50, 3, 4, 2, 546, 678, 213))