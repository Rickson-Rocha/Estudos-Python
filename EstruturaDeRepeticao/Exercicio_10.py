""" Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; """

validacao = False
while validacao==False:
    nome = input('Digite seu nome : ')
    idade = int(input('Digite sua idade'))
    sexo = input('informe seu sexo')
    salario = float(input('Informe seu salário: '))
    estado = input('informe seu estado civil: ')
    if(len(nome)>=3 and idade>0 and idade < 150 ):
        if(salario>0):
            if( sexo==' m ' or sexo==' f '):
                if( estado=='s' or estado=='c' or estado=='c' or estado=='v' or estado=='d'):
                    validacao=True
                    print('cadastro realizado')
                else:
                    print('Cadastro não realizado')
                    nome = input('Digite seu nome : ')
                    idade = int(input('Digite sua idade'))
                    sexo = input('informe seu sexo')
                    salario = float(input('Informe seu salário: '))
                    estado = input('informe seu estado civil: ')