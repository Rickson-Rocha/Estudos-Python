""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido. """
valorHora = float(input('Informe quanto você recebe por hora trabalhada: '))
numeroHora = float(input('Informe quantas horas você trabalhará esse mês:'))
calculoSalarioBruto = valorHora*numeroHora
descontoIr = (11/100*(calculoSalarioBruto))
descontoInss = (8/100*(calculoSalarioBruto))
descontoSindicato = (5/100*(calculoSalarioBruto))
salarioLiquido = calculoSalarioBruto - descontoIr - descontoInss - descontoSindicato

print('Seu salário bruto - sem descontos - é de {}'.format(calculoSalarioBruto))
print('Valor descontado IR: R$ {}'.format(descontoIr))
print('Valor descontado INSS: R$ {}'.format(descontoInss))
print('Valor descontado Sindicato: R$ {}'.format(descontoSindicato))
print('----------------------------------------------------')
print('Salário liquido: R$ {} '.format(salarioLiquido))