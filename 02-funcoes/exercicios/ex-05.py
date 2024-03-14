identificador = str(input("Digite seu identificador: "))

def is_identificador_valid(identificador: str):

    if len(identificador) != 7:
        return False
    if not f"{identificador[0]}{identificador[1]}" == "BR":
        return False
    if not int(identificador[2:6]):
        return False 
    if not identificador[len(identificador) - 1] == "X":
        return False
    
    return True

valido = "válido" if is_identificador_valid(identificador) else "inválido"

print(f"Seu identificador é {valido}.")