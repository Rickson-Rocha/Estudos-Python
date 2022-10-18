""" Escreva um programa para fazer uma pesquisa de opinião sobre a
satisfação no atendimento de uma farmácia. As opções de respostas
devem ser INSATISFEITO; SATISFEITO; NÃO QUERO RESPONDER. O
algoritmo deverá ainda perguntar quantas usuários irão responder à
pergunta. Ao final apresentar o percentual de resposta de cada opção. """

#3 
#1 usuário -> uma opção

# A - > insatisfeito
# B - > insatisfeito
# C ->  não quero responder

#calcular a porcentagem das respostas
#incrementa+
#insatisfeito 

numeroResposta = int(input('Quantas respostas você irá coletar: '))
contador = 1
satisfeito = 0
insatisfeito = 0
naoResponder = 0
while(contador <= numeroResposta):
  respostaUsuario = input('Digite sua opnião: ')
  if(respostaUsuario == 'satisfeito'):
    satisfeito = satisfeito + 1
    
  elif(respostaUsuario == 'insatisfeito'):
     insatisfeito = insatisfeito + 1
  elif( respostaUsuario == 'NÃO QUERO RESPONDER'):
    naoResponder = naoResponder + 1
  contador = contador + 1 
