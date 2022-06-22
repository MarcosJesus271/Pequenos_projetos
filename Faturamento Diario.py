#! Notas.......... Arquivo de faturamento disponibilizado é {dados.json}, para utiliza-lo deixe no mesmo diretorio do script.
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
print(("O menor valor de faturamento encontrado foi, \033[1;32mR$:%f\033[m") % (menor))
print(("O maior valor de faturamento encontrado foi, \033[1;32mR$:%f\033[m") % (maior))

# Descobrir media mensal
soma_valores = sum(listOfValues)
valor_dias = len(new_map)
media = soma_valores / valor_dias
print(("A média mensal calculada foi, \033[1;32mR$:%f\033[m") % (media))

print('\n')

#Descobrir os dias em que o valor de faturamento diário foi superior à media mensal
media = int(media)
valor_fatu =[]

for i in new_map:
    if i > media:
        valor_fatu.append(i)
    else:
        pass

num_dias = len(valor_fatu)
print(("Total de dias em que o Faturamento foi superior à media mensal, foram de: \033[1;32m%d dias.\033[m")%(num_dias))

