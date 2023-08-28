import math

#Delta = b² - 4.a.c
def valor_delta (a, b, c):
	delta = b**2 - 4*a*c 
	return delta

#-b +- raiz de A / 2.a 
def raiz_delta (a, b, c, delta):
    if delta < 0:
        return "Não foi possivel Calcular a Raiz de Delta pois o delta é menor que zero!"
    elif delta == 0:
        raiz_quadrada = -b / (2*a)
        return raiz_quadrada
    else:
        return [(-b + (math.sqrt(delta))) / (2 * a), (-b - (math.sqrt(delta))) / (2 * a)]

def calcular_delta (a, b, c):
    delta = valor_delta(a, b, c)
    return raiz_delta(a, b, c, delta)

#-----------------------------------------------------------------------

print("Valor da equação de segundo Grau")
a = float(input("Digite o valor de a"))
b = float(input("Digite o valor de b"))
c = float(input("Digite o valor de c"))

print (calcular_delta (a, b, c))