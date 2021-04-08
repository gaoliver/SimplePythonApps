import sys
import string
import random


# Funções

def space():
    print('')
    print('')
    print('')


def processo():
    vogais = ['A', 'E', 'I', 'O', 'U']
    consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                  'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    numbers = '2, 3, 4, 5, 6, 7, 8, 9, 10'
    let = 'let'
    prev = 0
    result = []
    nome = 'Nome criado: '

    confirm = 0

    # Quantidade de letras
    while (confirm == 0):

        qts = input('O nome terá quantas letras? ')

        if (str(qts) in numbers):
            space()
            confirm = 1

        else:
            space()
            print('Insira um valor correto. Somente números.')
            qts = input('O nome terá quantas letras? ')

    # Definindo as letras
    num = int(qts)
    y = 0
    esp = 0

    # Primeira letra
    if prev == 0:

        y += 1

        letra = let+str(y)

        i = 0

        i = random.choice(string.ascii_uppercase)

        prev = i

        exec(f'{letra} = i')

        num -= 1

        result.append(letra)


    # Outras letras
    while num > 0:

        y += 1

        letra = let+str(y)

        i = 0

        # Vogais
        if ((prev != 0) and (prev in consoantes)):

            i = random.randint(1, 3)

            vogal = vogais[i]

            prev = vogal

            exec(f'{letra} = vogal')

            num -= 1

            result.append(letra)

        # Consoantes
        elif ((prev != 0) and (prev in vogais)):

            i = random.randint(1, 19)

            consoante = consoantes[i]

            prev = consoante

            exec(f'{letra} = consoante')

            num -= 1

            esp = 1

            result.append(letra)

        # Consoantes Especiais
        elif ((prev != 0) and (prev in consoantes) and (esp == 1)):

            i = random.randint(1, 19)

            consoante = consoantes[i]

            prev = consoante

            exec(f'{letra} = consoante')

            num -= 1

            esp = 0

            result.append(letra)

    # Imprimir resultado
    resultado = 'nome'
    for r in result:
        resultado += '+'+r

    exec(f'{resultado}\nprint({resultado})')

    # saída
    sair()


# Função para sair

def sair():

    reiniciar = 0

    reiniciar = input('Gostaria de tentar novamente? (1)SIM e (2)NÃO: ')

    if reiniciar == '1':
        space()
        processo()
    elif reiniciar == '2':
        sys.exit()
    else:
        space()
        print('Opa! Responda exatamente o que foi proposto.')
        space()

        sair()



def intro():
    space()
    print('Bem-Vindo ao CRIADOR DE NOME!')
    print('.')
    print('Escolha a quantidade de letras e tenha um nome super-legal.')


# Iniciar programa
intro()
processo()
