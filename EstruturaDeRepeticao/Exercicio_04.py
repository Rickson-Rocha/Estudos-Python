""" Escreva um algoritmo que solicite ao usuário um número entre 1 e 10000 e
depois informe para o usuário se o número digitado é primo. Um número é dito
ser primo quando ele é divisível apenas por 1 e ele mesmo. """

numero  =  int(input('Digite um número')) #3
contador = 1
qtdDivisores = 0
  #Estabeleci a condição de intervalo número no próprio laço
while(contador<=numero and numero>=1 and numero<=10000):
    if(numero%contador == 0):
      qtdDivisores = qtdDivisores +1
    contador = contador +1
if(qtdDivisores<=2 and numero!=1):
    print(' {} é um número é primo'.format(numero))
else:
    print('{} não é um número primo'.format(numero))