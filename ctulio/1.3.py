''' # Trabalhando com diferença de versão
try:
    nome = raw_input('Digite seu nome: ') #python2  
    ## função input(), no Python 2, não transforma a entrada do usuário em string, mas tenta avaliar, calcular ela
except:
    nome = input('Digite seu nome: ')     #python3
    idade = input('Digite sua idade: ')
'''

sg_partido = ['PSOL', 'PTB', 'MDB', 'ARENA']
sg_partido_b = []
sg_partido_indefinida = []

for sigla in sg_partido:
    if sigla[0] == 'P':
        sg_partido_b.append(sigla)
    else:
        sg_partido_indefinida.append(sigla)

print(sg_partido_b, sg_partido_indefinida)
