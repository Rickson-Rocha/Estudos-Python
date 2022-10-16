""" Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """
verificador = input('Informe seu gênero:')
if(verificador == 'M' | verificador=='m'):
    print('Sexo masculino')
elif (verificador == 'F' | verificador =='f'):
    print('Sexo feminino')
else:
    print('sexo inválido')    