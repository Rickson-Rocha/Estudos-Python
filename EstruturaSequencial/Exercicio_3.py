""" Faça um Programa que peça dois números e imprima a soma.
 """
i = 1
soma = 0
while( i < 3):
    numero = int(input('Digite o {} º'.format(i)))
    soma = numero + soma
    i = i +1
else:
    print('A soma dos número é {}'.format(soma))
