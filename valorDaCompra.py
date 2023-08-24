#Valor da Compra

precoUnit = 100
numeroCompra = 2

if (numeroCompra > 20):
	desconto = 20;
	unidade = precoUnit - (precoUnit*desconto / 100)
	valor = unidade * numeroCompra
	print (f"O valor com desconto é R$ {unidade} e total R$: {valor}")
 
elif (numeroCompra >= 11):
	desconto = 10;
	unidade = precoUnit - (precoUnit*desconto / 100)
	valor = unidade * numeroCompra
	print (f"O valor com desconto é R$ {unidade} e total R$: {valor}")

else:
	valor = precoUnit * numeroCompra
	print (f"O valor unitário é {precoUnit} e o Valor Total é R$ {valor}")