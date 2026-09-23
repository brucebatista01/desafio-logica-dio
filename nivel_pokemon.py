pokemon = "Pikachu"
xp = 10050
nivel_rank = ""

if xp < 1000:
    nivel_rank = "Ferro"
elif xp >= 1001 and xp <= 2000:
    nivel_rank = "Bronze"
elif xp >= 2001 and xp <= 5000:
    nivel_rank = "Prata"
elif xp >= 5001 and xp <= 7000:
    nivel_rank = "Ouro"
elif xp >= 7001 and xp <= 8000:
    nivel_rank = "Platina"
elif xp >= 8001 and xp <= 9000:
    nivel_rank = "Ascendente"
elif xp >= 9001 and xp <= 10000:
    nivel_rank = "Imortal"
elif xp >= 10001:
    nivel_rank = "Radiante"

print(f"O Herói de nome {pokemon} está no nível de {nivel_rank}")
