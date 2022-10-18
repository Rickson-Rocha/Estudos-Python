""" Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: """



nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
somador = nota1 + nota2
  
media = somador/2
if(media >=9 and media <=10):
  print('Nota 1: {} | Nota 2: {} | Media: {} | Conceito A | Situação : Aprovado'.format(nota1,nota2,media))
elif (media>=7.5 and media <9):
  print('Nota 1: {} | Nota 2: {} | Media: {} | Conceito B | Situação : Aprovado'.format(nota1,nota2,media))
elif(media>=6.0 and media < 7.5):
  print('Nota 1: {} | Nota 2: {} | Media: {} | Conceito C | Situação : Aprovado'.format(nota1,nota2,media))
elif (media >= 4 and media < 6):
  print('Nota 1: {} | Nota 2: {} | Media: {} | Conceito D | Situação : Reprovado'.format(nota1,nota2,media))
elif(media >= 0 and media < 4):
  print('Nota 1: {} | Nota 2: {} | Media: {} | Conceito E |Situação : Reprovado'.format(nota1,nota2,media))
  