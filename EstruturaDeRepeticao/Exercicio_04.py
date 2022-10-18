""" Escreva um algoritmo que solicite ao usuário um número entre 1 e 10000 e
depois informe para o usuário se o número digitado é primo. Um número é dito
ser primo quando ele é divisível apenas por 1 e ele mesmo. """

numero = int(input('Digite um número : '))
contador = 1
while(contador < 10000):
    if(numero % contador == 0):
        print('o número informado é primo')
    contador = contador +1    
else:
    print('Numero informado está fora do intervadlo  [1 , 10000]')        
