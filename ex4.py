fat_mensal = {
    "sp": 67836.43,
    "rj": 36678.66,
    "mg": 29229.22,
    "es": 27165.48,
    "outros": 19849.53
}

def calc_percentual(fat_mensal: dict[str, float], estado: str) -> float:
    percentual = (fat_mensal[estado] / sum(fat_mensal.values())) * 100
    return round(percentual, 2)

print(calc_percentual(fat_mensal, 'es'))
