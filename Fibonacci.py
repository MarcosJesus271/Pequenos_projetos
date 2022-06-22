fibo = [1,1]
i = 0
verf = int(input("Digite o número que deseja pesquisar: "))
num = int(input("Digite em quantos termos da sequencia devo pesquisar: "))

while num > len(fibo):
	fibo.append(fibo[i] + fibo[i+1])
	i+=1

lista = fibo
print(lista)

try:
    if lista.index(verf):
        print('Encontrado! O número %d pertence a sequencia Fibonacci'%(verf))
except:
    print("Não encontrado! O número %d não pertence a sequencia Fibonacci ou altere a quantidade de termos para uma nova busca" % (verf))