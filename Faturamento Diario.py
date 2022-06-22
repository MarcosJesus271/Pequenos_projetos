import json

f = open('dados.json')
data = json.load(f)
dias=[]
valores=[]

for i in data:
    dia = i
    valor = i
    dias.append(dia['dia'])
    valores.append(valor['valor'])
dict_from_list = {dias[i]: valores[i] for i in range(len(dias))}

# Mapear numeros maior valor de faturamento e o menor valor de faturamento, eliminando os dias sem faturamento.
listOfValues = dict_from_list.values()
listOfValues = list(listOfValues)
seen = {0}
new_map = []
for item in listOfValues:
    try:
        flitem = float(item)
    except ValueError:
        continue
    if flitem not in seen:
        seen.add(flitem)
        new_map.append(item)

maior = max(new_map)
menor = min(new_map)
print(("O menor valor de faturamento encontrado foi, R$:%f ") % (menor))
print(("O maior valor de faturamento encontrado foi, R$:%f ") % (maior))

# Descobrir media mensal
soma_valores = sum(listOfValues)
valor_dias = len(new_map)
media = soma_valores / valor_dias
print(("A média mensal calculada foi, R$:%f") % (media))
# R$:20865.370167

#Descobrir os dias em que o valor de faturamento diário foi superior à media mensal
if media < listOfValues:
    print(listOfValues)
