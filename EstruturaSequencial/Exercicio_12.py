""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
 """
homemAltura = float(input('informe sua altura:'))
calculoHomem = (72.7*homemAltura) - 58
print('Seu peso ideal é {}'.format(calculoHomem))
mulherAltura = float(input('informe sua altura:'))
calculoMulher = (72.7*mulherAltura) - 58
print('Seu peso ideal é {}'.format(calculoMulher))
