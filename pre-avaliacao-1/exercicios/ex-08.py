def contar_palavras(frase: str):
    contagem_palavras = {}
    
    for invalido in (".", ",", "/", "?", "!", "'", "0", "1", "2", "3", "4", "6", "7", "8", "9"):
        frase = frase.replace(invalido, "")

    frase = frase.split(" ")

    for palavra in frase:
        contagem_palavras[palavra] = frase.count(palavra)

    return contagem_palavras

frase = input("Digite uma frase para contar as palavras: ")
print(contar_palavras(frase))