valor_compra = float(input("Digite o valor da compra: "))

def desconto(valor):

    if valor >= 500.0:
        return 0.15
    if valor <= 499.99 and valor >= 100.0:
        return 0.1
    if valor <= 99.99 and valor >= 10.0:
        return 0.05
    
    return 0.0

print(f"Valor final: {valor_compra - (valor_compra * desconto(valor_compra))}")
print(f"Desconto aplicado: {int(desconto(valor_compra) * 100)}%")