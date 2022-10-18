""" 1. O cálculo do fatorial de um número é dado pela multiplicação desse
número com todos os antecessores inteiros positivos. Por exemplo, o
fatorial de 5 é 5! = 5*4*3*2*1 = 120. Escreva um programa que
solicite um número e apresente o resultado do seu fatorial. """

num = int(input('Digite o número o qual você deseja calcular o fatorial')) #5
multiplicador = num-1 #4
while(multiplicador > 1):
    num = num * (multiplicador) #20 #60 #120
    multiplicador = multiplicador - 1 #3 #2
print(num)    

#outra forma

n = int(input('Digite um número : ')) #4
contador = 1
while( contador < n):
    mult = n* contador 
    contador = contador + 1