""" Faça um Programa que leia três números e mostre-os em ordem decrescente.
 """
numero1 = int(input('informe um número'))
numero2 = int(input('informe um número'))
numero3 = int(input('informe um número'))
ordem = [numero1,numero2,numero3]
ordem.sort(reverse = True)
print(ordem)