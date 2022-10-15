
""" Faça um Programa que peça as 4 notas bimestrais e mostre a média. """
contador = 1
soma = 0
while (contador <= 4):
  numero = int(input('Digite a {}º nota:'.format(contador)))
  soma = soma + numero
  contador = contador + 1
else:
  media = soma / (contador - 1)
  print("Sua média é {}".format(media))
