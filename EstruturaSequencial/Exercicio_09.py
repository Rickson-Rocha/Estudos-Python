""" Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius """
print('conversor de tempetura F -> C')
fahrenheit= float(input('Informe  a temperatura em Fahrenheit'))
calculo = 5 * ((fahrenheit-32) / 9)
print('A temperatura {} equivale a {} celsius'.format(fahrenheit,calculo))