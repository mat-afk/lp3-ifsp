nota = float(input("Digite uma nota (de 0 a 100) para converter: "))

def converter_nota(nota):

    if nota < 0.0 or nota > 100.0:
        return "Nota inválida"

    if nota >= 90.0:
        return "A"
    if nota < 90.0 and nota >= 80.0:
        return "B"
    if nota < 80.0 and nota >= 70.0:
        return "C"
    if nota < 70.0 and nota >= 60.0:
        return "D"

    return "F"

print(f"Nota: {converter_nota(nota)}")