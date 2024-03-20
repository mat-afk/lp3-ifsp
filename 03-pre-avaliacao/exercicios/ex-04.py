votos = {
    "Luiz Inácio Lula da Silva": 0,
    "José Serra Chirico": 0,
    "Anthony Garotinho": 0,
}

print("ELEIÇÕES 2002\n")
print("Candidatos: ")

for candidato in votos:
    print(candidato)
print()
    
for i in range(0, 2):
    voto = input("Vote em um candidato: ")

    if voto in votos:
        votos[voto] += 1

print("\nContagem de votos: ")
for candidato in votos:
    print(f"{candidato}: {votos[candidato]}")

print(f"\nCandidato vencedor: {max(votos)}")