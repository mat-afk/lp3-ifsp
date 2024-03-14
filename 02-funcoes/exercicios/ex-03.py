valor_compra = 0.00
while valor_compra <= 0.00:
    valor_compra = float(input("Digite o valor da compra: "))

def get_desconto(valor):

    if valor >= 500.0:
        return 0.15
    if valor <= 499.99 and valor >= 100.0:
        return 0.1
    if valor <= 99.99 and valor >= 10.0:
        return 0.05
    
    return 0.0

print(f"Valor final: R$ {valor_compra - (valor_compra * get_desconto(valor_compra))}")
print(f"Desconto aplicado: {int(get_desconto(valor_compra) * 100)}%")