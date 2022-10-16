""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """
produto = int(input('informe o valor do produto '))
contador = 1
while contador < 3:
  produtoLaco = int(input('informe o valor do produto: '))
  if (produtoLaco < produto):
    produto = produtoLaco
  contador = contador + 1
print('O produto a ser comprado tem o valor de R$ {} '.format(produto))