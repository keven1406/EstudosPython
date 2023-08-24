#FATORIAL

def fatorial (numero):
  controladora = numero - 1
  multiplicador = numero
  produto = 0
  while controladora > 0:
    multiplicador *= controladora
    produto = multiplicador
    controladora -= 1
  return produto

  #funcao recursiva
  def fatorial_recursivo(numero):
    if (numero == 1) or (numero == 0)
      return 1
    return fatorial_recursivo(n*fatorial_recursivo(n-1)) #n é a variavel global da inserção do usuario
    

#-------------------------------------------------------
numero_inserido = eval(input("Digite um numero para obter seu fatorial: "))
numero = 0

if numero_inserido == 1 or numero_inserido == 0:
  numero = 1
else:
  numero = fatorial(numero_inserido)

print(f"O fatorial de !{numero_inserido} é : {numero}")