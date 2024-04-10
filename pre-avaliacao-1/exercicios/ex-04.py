candidatos = [
    {
        "nome": "Candidato 1",
        "numero": "13",
        "votos": 0,
    },
    {
        "nome": "Candidato 3",
        "numero": "14",
        "votos": 0,
    },
    {
        "nome": "Candidato 2",
        "numero": "15",
        "votos": 0,
    },
]

print("ELEIÇÕES 2024")
print("Candidatos: ")

for candidato in candidatos:
    print(f"{candidato["nome"]}: {candidato["numero"]}")

for i in range(2):
    voto = input("Vote em um candidato: ")

    for candidato in candidatos:
        if voto == candidato["numero"]:
            candidato["votos"] += 1

vencedor = {
    "nome": "",
    "numero": "0",
    "votos": 0
}

print("Resultados da votação: ")

for candidato in candidatos:
    print(f"{candidato["nome"]}: {candidato["votos"]}")

    if candidato["votos"] > vencedor["votos"]:
        vencedor = candidato

print(f"{vencedor["nome"]} foi eleito!")
print(f"Número eleitoral: {vencedor["numero"]}")
print(f"Total de votos: {vencedor["votos"]}")