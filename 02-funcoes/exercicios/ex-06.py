comprimento = float(input("Digite o comprimento do aquário: "))
altura = float(input("Digite a altura do aquário: "))
largura = float(input("Digite a largura do aquário: "))
temperatura_desejada = float(input("Digite a temperatura desejada para seu aquário: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente: "))

def get_volume(comprimento, altura = 1, largura = 1):
    return comprimento * altura * largura / 1000

def get_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def get_filtragem_por_hora(volume):
    return volume * 2, volume * 3

volume = get_volume(comprimento, altura, largura)
print(f"Volume: {volume}L")
print(f"Potência do termostato: {get_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)}W")
print(f"Filtragem por hora: {get_filtragem_por_hora(volume)[0]}L a {get_filtragem_por_hora(volume)[1]}L")