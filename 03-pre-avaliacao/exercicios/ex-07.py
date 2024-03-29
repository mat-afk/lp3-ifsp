from random import choice

print("---------------------------")
print("BEM-VINDO AO JOGO DA FORCA")
print("---------------------------")

palavras = (
    "python",
    "programacao",
    "desenvolvimento",
    "computador",
    "tecnologia",
    "batata",
    "java"
)

palavra_oculta = choice(palavras).lower()
palpite = ["_" for _ in palavra_oculta]
vidas = 3
letras_tentadas = []

while vidas > 0:
    print(f"Você tem {vidas} vida(s)")
    print(" ".join(palpite))

    if "".join(palpite) == palavra_oculta:
        print("Você acertou!")
        break

    if letras_tentadas:
        print(f"letras tentadas: {" ".join(letras_tentadas)}")
    letra_palpite = input("digite uma letra: ").lower()

    if letra_palpite not in palavra_oculta:
        vidas -= 1
        letras_tentadas.append(letra_palpite)
        print("letra incorreta!")
    else:
        for i in range(len(palavra_oculta)):
            if palavra_oculta[i] == letra_palpite:
                palpite[i] = letra_palpite
else:
    print(f"Você não tem mais tentativas. A palavra era: {palavra_oculta}")