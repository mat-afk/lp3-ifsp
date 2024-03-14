peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

def get_imc(peso, altura):
    return peso / altura ** 2

def get_classificacao(imc):

    if imc < 18.5:
        return "Baixo peso"
    if imc < 25.0:
        return "Peso normal"
    if imc < 30.0:
        return "Excesso de peso"
    if imc < 35.0:
        return "Obesidade de classe 1"
    if imc < 40.0:
        return "Obesidade de classe 2"
    
    return "Obesidade de classe 3"

def get_peso_a_perder(peso, altura):
    return peso - (24.9 * altura * altura)

imc = get_imc(peso, altura)
peso_a_perder = round(get_peso_a_perder(peso, altura))

print(f"IMC: {imc:.1f}")
print(f"Classificação: {get_classificacao(imc)}")
print(f"Você precisa {"perder" if peso_a_perder >= 0.0 else "ganhar"} {peso_a_perder if peso_a_perder >= 0.0 else peso_a_perder * -1}kg para chegar ao peso normal.")