
""" Faça um Programa que leia três números e mostre o maior e o menor deles. """
numero = int(input('informe o valor do produto '))
contador = 1
maiorNumero =0
while contador < 3:
  numeroLaco = int(input('informe o numero: '))
  if (numeroLaco < numero):
    numero = numeroLaco
  elif(numeroLaco > maiorNumero):
     maiorNumero = numeroLaco
  contador = contador + 1
 
print('maior numero informado {} '.format(maiorNumero))
print('menor numero informado {} '.format(numero))