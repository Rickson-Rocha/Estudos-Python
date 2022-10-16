""" Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez. """
contador = 1
somador = 0
while contador < 3:
    nota = int(input('informe a nota : '))
    somador = somador + nota
    contador = contador + 1
media = somador/2
if(media >= 7 and media < 10):
    print('aprovado')
elif (media >= 10):
    print('Aprovado com distinção')
else:
    print('reprovado')      