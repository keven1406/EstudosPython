#ESTRATEGIA 1 - ESTRUTURAL

lista = [10, 2, 5, 7 , 6, 3]

n = len(lista) #len() = numero total de indices na lista
soma = 0

for i in range(n):
	if (lista[i] % 2 == 0):
		soma = soma + lista[i]
print (f"O somatório dos elementos pares da lista é: {soma}")


-------------------------------------------------------------------

#ESTRATEGOA 2 - FUNCIONAL

lista = [10, 2, 5, 7 , 6, 3]

n = len(lista) #len() = numero total de indices na lista
soma = 0

for num in lista:
	if (num % 2 == 0):
		soma = soma + num
print (f"O somatório dos elementos pares da lista é: {soma}")