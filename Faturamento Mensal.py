sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
outros = float(19.84953)
total = float(sp + rj + mg + es + outros)

psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((outros/total)*100)

print('Porcentagem de SP \033[1;32m{}\033[m'.format(psp))
print('Porcentagem de RJ \033[1;32m{}\033[m'.format(prj))
print('Porcentagem de MG \033[1;32m{}\033[m'.format(pmg))
print('Porcentagem de ES \033[1;32m{}\033[m'.format(pes))
print('Porcentagem de OUTROS \033[1;32m{}\033[m'.format(pout))