""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo. """

inteiroUm = int(input('Digite um número inteiro'))
inteiroDois = int(input('Digite um segundo número'))
numReal =  float(input('Digite um número real:'))
calculoUm = (inteiroUm*(inteiroDois/2))
calculoDois = ((inteiroUm*3)+ (numReal*3))
calculoTres = numReal**3
print(calculoUm)
print(calculoDois)
print(calculoTres)