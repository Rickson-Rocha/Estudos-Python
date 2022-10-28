""" Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

validador = False
while validador!=True:
    login =input('Login: ')
    senha =input( 'senha: ')
    if(login==senha):
        validador = True
        print('Error: Login e usuário idênticos')
    login =input('Login: ')
    senha =input('senha: ')
else:
     print('Usuário autênticado')    