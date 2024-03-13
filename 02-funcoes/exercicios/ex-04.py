def validar_identificador(identificador: str):
    if len(identificador) != 7:
        return False
    if not f"{identificador[0]}{identificador[1]}" == "BR":
        return False
    if not int(identificador[2:6]):
        return False 
    if not identificador[len(identificador) - 1] == "X":
        return False
    return True
