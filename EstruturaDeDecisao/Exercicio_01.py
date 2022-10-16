""" Faça um Programa que peça dois números e imprima o maior deles. """
contador = 1
maiorNumero = 0
while contador < 4:
    num =  int(input('Digite o {}º número: '.format(contador)))
    if(num > maiorNumero):
        maiorNumero = num
    contador += 1
print(maiorNumero)