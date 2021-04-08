# encoding: UTF-8
import sys
import random
import time


numbers = '101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899'


# Definições

def space():
    print(' ')
    print(' ')
    print(' ')


def progress_bar(value, max, barsize):
   chars = int(value * barsize / float(max))
   percent = int((value / float(max)) * 100)
   sys.stdout.write("#" * chars)
   sys.stdout.write(" " * (barsize - chars + 2))
   if value >= max:
      sys.stdout.write("pronto. \n\n")
   else:
      sys.stdout.write("[%3i%%]\r" % (percent))
      sys.stdout.flush()

def carregamento():
    for i in range(8):
        progress_bar(i, 7, 50)
        time.sleep(1)



# O programa

def choice():
    # Variáveis

    pergunta = str(input('Digite a pergunta que te deixa em dúvida: '))

    space()

    qts = 0
    num = 0
    op = 'option'
    y = 0
    opcoes = []




    qts = input('Quantas opções você tem? ')

    verification = 0

    if (str(qts) in numbers) and (int(qts) != 0):
        num = int(qts)
        verification = 1

    while verification == 0:
        space()
        print('Digite uma resposta válida. Somente números.')
        qts = input('Quantas opções você tem? ')
        if (str(qts) in numbers):
            num = int(qts)
            verification = 1


    qts = int(qts)



    # Função

    while qts > 0:
        y += 1
        op = str(input(f'Opção {y}: '))
        opcoes.append(op)
        qts -= 1

    space()



    # Resultado

    carregamento()

    resultado = random.choice(opcoes)

    print(pergunta+'? '+resultado)


    space()

    exit()



# Finalizando

def exit():

    reiniciar = input('Deseja FAZER NOVAMENTE? (1) para SIM e (2) para NÃO: ')

    if reiniciar == '1':
        space()
        choice()
    elif reiniciar == '2':
        sys.exit()
    else:
        space()
        print('Opa! Responda exatamente o que foi proposto.')
        space()

        exit()




# Iniciando

space()

print('Bem-vindo ao CHOICE! Hora de esquecer a dúvida e partir para a certeza.')

space()

click = input('Clique ENTER para continuar...')

space()

choice()