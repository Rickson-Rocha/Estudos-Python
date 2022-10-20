""" Escreva um programa para fazer uma pesquisa de opinião sobre a
satisfação no atendimento de uma farmácia. As opções de respostas
devem ser INSATISFEITO; SATISFEITO; NÃO QUERO RESPONDER. O
algoritmo deverá ainda perguntar quantas usuários irão responder à
pergunta. Ao final apresentar o percentual de resposta de cada opção. """
numeroResposta = int(input(' Infome quantas  respostas você quer registrar :'))
contador = 1
satisfeito = 0
insatisfeito = 0
naoResponder = 0
while contador <= numeroResposta:
    respostaUsuario = input('Registre sua opnião :')
    if (respostaUsuario == 'satisfeito' or respostaUsuario == 'SATISFEITO'
        or respostaUsuario == 'Satisfeito'):
      satisfeito = satisfeito + 1
    elif (respostaUsuario == 'insatisfeito' or respostaUsuario == 'INSATISFEITO'
          or respostaUsuario == 'Insatisfeito'):
      insatisfeito = insatisfeito + 1
    elif (respostaUsuario == 'não quero responder'
          or respostaUsuario == 'NÃO QUERO RESPONDER'
          or respostaUsuario == 'Não quero responder'):
      naoResponder = naoResponder + 1
    contador = contador + 1
  
totalRespostas = satisfeito + insatisfeito + naoResponder
  
calcSts = (satisfeito / totalRespostas) * 100
calcIts = (insatisfeito / totalRespostas) * 100
calcNr = (naoResponder / totalRespostas) * 100
print('Total de respostas registradas : {} '.format(totalRespostas))
  
print('Satisfeito {} %'.format(calcSts))
print ('Insatisfeito {} % '.format(calcIts))
sprint ('Optaram por não responder {} %'.format(calcNr))
