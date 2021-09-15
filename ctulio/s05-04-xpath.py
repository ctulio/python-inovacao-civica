## SELETORES

# raiz
//

# Todos os elementos 'div' descendentes da raiz
//div

# Elemento 'p' descendentes imediatos de elementos 'div'
//div/p

# Todos os elementos 'p' descendentes de elementos 'div'
//div//p

#Ascendente imediato de elementos 'p'
//p/..


## ATRIBUTOS

# Atributos 'href' de todos os elementos 'a'
//a/@href

# Textos dentro de todos os elementos descendentes de elementos 'p'
//p//text()

# Textos dentro de todos os elementos 'p' 
//p/text()


## CONDIÇÕES

# Elementos 'p' com texto igual a 'Olá'
//p[text()="Olá"]

# Elementos 'p' com text contendo a string 'xis'
//p[contains(text(),"xis")]

# Elementos "item" com atributo "price" maior que "2.50"
//item[@price>2.50]

# Elementos "item" com atributo "price" maior que "2.50" e menor ou igual a "3"
//item[@price>2.50 and @price<=3]


## ORDENAÇÃO

# Segundo 'p' descendente imediato de elementos 'h1'
//h1/p[2]

# Último 'p' descendente imediato de elementos 'h1'
//h1/p[last()]

# Elementos 'p' que possuem atributo 'id' igual a 'id' e são
# primeiro descendente imediato de elementos 'h1'
//h1/p[1][@id="id"]



http://www.procedebahia.com.br/ba/caetite/edicoes
# Gabarito
//div[@id='edicoes']/ul/li[1]/a/@href
//div/ul/li[@class="data"]/a/@href
