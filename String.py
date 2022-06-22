str=input('Digite uma palavra ou uma frase: ')
reversed_string=''.join(reversed(str))

print("Ela invertida é: \033[1;32m%s\033[m" %(reversed_string))  