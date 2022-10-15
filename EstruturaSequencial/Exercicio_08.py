""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. """
valorHora = float(input('Quanto você ganha por hora de trabalho?'))
horaMes = float(input('Quantas horas você trabalhou no mês'))
calculoSalario = valorHora*horaMes
print('Salário total  R$ {}'.format(calculoSalario))