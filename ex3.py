import json

with open("./dados.json", "r") as file:
    dados = json.load(file)

def calc_faturamento(data):
    valores = [x["valor"] for x in data]
    maior_valor_faturamento = max(valores)
    menor_valor_faturamento = min(valores)

    avg = sum(valores) / len(valores)

    dias_com_faturamento_superior_media = [x["dia"] for x in data if x["valor"] > avg]

    return (maior_valor_faturamento, menor_valor_faturamento, dias_com_faturamento_superior_media)





print(calc_faturamento(dados))