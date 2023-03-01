import json

with open ('dados.json') as file:
    dados_dict = json.load(file)

menor = 0
for i in range(len(dados_dict)):
    menor = dados_dict[i]['valor']
    for k in range(len(dados_dict)):
        if menor > dados_dict[k]['valor']:
            menor = dados_dict[k]['valor']
print('o menor valor é:', menor)


maior = 0
for i in range(len(dados_dict)):
    maior = dados_dict[i]['valor']
    for k in range(len(dados_dict)):
        if maior < dados_dict[k]['valor']:
            maior = dados_dict[k]['valor']
print('o maior valor é:', maior)

total = 0
for i in range(len(dados_dict)):
    total += dados_dict[i]['valor']

media = total/30
numero_dias = []
for i in range(len(dados_dict)):
    if media < dados_dict[i]['valor']:
        numero_dias.append(dados_dict[i]['dia'])

print('O dias em que o faturamento diário foi superior à media mensal: ',numero_dias)

