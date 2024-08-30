# NAO HOUVE JSON OU XML DISPONIVEL

def calc_faturamento(vect: list[float]) ->tuple[float, float, int]:
    maior_valor_faturamento = max(vect)
    menor_valor_faturamento = min(vect)

    dias_com_faturamento_superior_media = len([fat for fat in vect if fat > (sum(vect) / len(vect))])

    return (maior_valor_faturamento, menor_valor_faturamento, dias_com_faturamento_superior_media)



fat_mensal = [67836.43, 36678.66, 29229.22, 27165.48, 19849.53]

print(calc_faturamento(fat_mensal))