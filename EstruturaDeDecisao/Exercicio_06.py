""" Faça um Programa que leia três números e mostre o maior deles. """
contador = 1
maiorNumero = 0
while contador < 4:
    num = int(input('Informe o {}º número'.format(num)))
    if(num > maiorNumero):
        maiorNumero = num
    contador += 1
print('O maior número fornecido foi : '.format(maiorNumero))    
