from random import randint
# funcoes
def peso_cromossomo(cromossomo, peso): 
    peso_sum = 0
    itens_qtd = len(peso)
    n = 0
    if (len(cromossomo) != itens_qtd):
        n = 2
    else:
        n = 0
    for i in range(itens_qtd):
        if cromossomo[n] == 1:
            peso_sum += peso[i]
        n = n + 1
    return peso_sum

def cromossomo_valor(cromossomo, valor): 
    sum_valor = 0
    itens_qtd = len(valor)
    if (len(cromossomo) != itens_qtd):
        n = 2
    else:
        n = 0
    for i in range(itens_qtd):
        if cromossomo[n] == 1:
            sum_valor += valor[i]
        n = n + 1
    return sum_valor
def populacao_gerar(tamanho_da_populacao, peso, valor, cap_max, itens_qtd): 
	populacao = []
	cromossomo = []
	for i in range(tamanho_da_populacao):
		if i%2==0:
			cromossomo = [randint(0,1) for n in range(itens_qtd)]
			cap = peso_cromossomo(cromossomo, peso)
			n = (itens_qtd-1) 
			while (cap > cap_max):
				cromossomo.pop(n)
				cromossomo.insert(n, 0)
				cap = peso_cromossomo(cromossomo, peso)
				n -= 1
			cap = peso_cromossomo(cromossomo, peso)
			val = cromossomo_valor(cromossomo, valor)
			populacao.append(cromossomo)
			populacao[i].insert(0, val)
			populacao[i].insert(1, cap)
		else:
			cromossomo = [randint(0,1) for n in range(itens_qtd)]
			cap = peso_cromossomo(cromossomo, peso)
			n = 0 
			while (cap > cap_max):
				cromossomo.pop(n)
				cromossomo.insert(n, 0)
				cap = peso_cromossomo(cromossomo, peso)
				n += 1
			val = cromossomo_valor(cromossomo, valor)
			populacao.append(cromossomo)
			populacao[i].insert(0, val)
			populacao[i].insert(1, cap)
	populacao.sort(reverse=True)
	return populacao
def mutacao(cromossomo, tx_mut): 
	itens_qtd = (len(cromossomo)+(-1-2))
	corte_inicial = randint(2,itens_qtd) 
	corte_fim = corte_inicial + tx_mut 
	while (corte_inicial < corte_fim):
		if corte_fim > itens_qtd:  
			corte_fim = itens_qtd 
		if cromossomo[corte_inicial] == 1:
			cromossomo.pop(corte_inicial)
			cromossomo.insert(corte_inicial, 0)
		elif cromossomo[corte_inicial] == 0:
			cromossomo.pop(corte_inicial)
			cromossomo.insert(corte_inicial, 1)
		corte_inicial += 1
	corte_inicial = 0
	return cromossomo
def crossover(populacao, taxa_de_mutacao, peso, valor, itens_qtd, cap_max):
   
    tamanho_da_populacao = len(populacao)
    corte = randint(5,itens_qtd-1)
    i = 0
    while(i < (tamanho_da_populacao - 1)):
        filho1 = populacao[i][2:corte] + populacao[i+1][corte:]
        filho2 = populacao[i+1][2:corte] + populacao[i][corte:] 

        filho1 = mutacao(filho1, taxa_de_mutacao)
        filho2 = mutacao(filho2, taxa_de_mutacao)

        cap = peso_cromossomo(filho1, peso)
        val = cromossomo_valor(filho1, valor)

        cap2 = peso_cromossomo(filho2, peso)
        val2 = cromossomo_valor(filho2, valor)
        if (cap <= cap_max and val > populacao[i][0]):
            populacao.pop(i)
            populacao.insert(i, filho1)
            populacao[i].insert(0, val)
            populacao[0].insert(i, cap)
        i += 1
        if (cap2 <= cap_max and val2 > populacao[i][0]):
            populacao.pop(i)
            populacao.insert(i, filho2)
            populacao[i].insert(0, val2)
            populacao[0].insert(i, cap2)
        i += 1
    populacao.sort(reverse=True)
    return populacao


file = open('kp_5000_24805.circ')
arquivo = file.read() 
instancias = arquivo.split() 

qtd_instancias = (len(instancias))
valor = []
peso = []

for i in range(2, qtd_instancias, 2):
    valor.append(int(instancias[i]))

for i in range(3,qtd_instancias,2):
    peso.append(int(instancias[i]))

tamanho_da_populacao = 4
taxa_de_mutacao = 2  
cap_max = int(instancias[1])
itens_qtd = int(instancias[0])
maximo_de_geracao = 4
atual_geracao = 1
maximo_de_geracao = 10
populacao = []


populacao = populacao_gerar(tamanho_da_populacao, peso, valor, cap_max, itens_qtd)

while (atual_geracao != maximo_de_geracao+1):
	print("Geracao: ", atual_geracao)
	populacao = crossover(populacao, taxa_de_mutacao, peso, valor, itens_qtd, cap_max)
	atual_geracao += 1

print("Melhor solucao da geracao ", atual_geracao-1)
print("Valor: ", populacao[0][0]," Peso: ", populacao[0][1])
print("Cromossomo", populacao[0][2:])