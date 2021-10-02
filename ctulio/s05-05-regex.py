import re

texto = "Querido Diário, hoje eu..."

diario = re.search(r"[dD]iário", texto)
print(diario.group())

reticencias = re.search(r"\.{3}", texto)
print(reticencias.group())
print(reticencias)

pontos = re.findall(r"\.", texto)
print(pontos)



# ============================================
l = ('89', '85', '1988','pastel', 'pato', \
	 '88', '859', '78','1932', '65',\
	 '82', '1981')

s = r'198[0-9]{1}'
# s = r'p.*'

# Ocorre erro na impressão quando não encontra um padrão
# for num in l:
# 	print(re.search(s, num).group())


# O if funciona como um teste, evitando o erro
# caso não exista o padrão buscado
for num in l:
	if re.search(s, num):
		print(re.search(s, num).group())
