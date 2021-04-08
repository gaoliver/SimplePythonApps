title = 'futuros salários'
print(title.upper())
print('Descubra todos os seus futuros salários.')

print(' ')

nome = input('Qual é o seu nome? ')
ini = float(input('Digite seu salário inicial: '))
ano1 = int(input('Ano inicial: '))
anof = int(input('Ano final: '))
ano2 = int(input('Ano do primeiro aumento: '))
a1 = float(input('Porcentagem do primeiro aumento: '))
ano3 = int(input('Ano do segundo aumento: '))
a2 = float(input('Porgentagem do segundo: '))

q1 = input('Existirá mais aumento com outra porcentagem? ')

eco = 0
stop = 0
a1 = a1/100
a2 = a2/100

if q1 == 'sim' :
    ano4 = int(input('Ano do próximo aumento: '))
    a3 = float(input('Porcentagem do próximo aumento: '))
    aumfinal = ano4
    rf = a3
else :
    aumfinal = ano3
    rf = a2


q2 = input('O aumento de {} continuará se renovando em outros anos? ' .format(aumfinal))


if q2 == 'sim' :
    r = int(input('De quantos em quantos anos? '))
    s = float(input('Quantas vezes maior que a porcentagem anterior? '))


x = float(input('Qual porcentagem você pretende economizar mensalmente? '))


print(' ')


while ano1 < ano2 :
    eco = eco + ((x / 100) * ini)
    print('{} - R${}'.format(ano1, ini))
    ano1 = ano1 + 1


if ano1 == ano2 :
    ini = ini + (ini * a1)

while ano1 >= ano2 and ano1 < ano3 :
    eco = eco + ((x / 100) * ini)
    print('{} - R${}'.format(ano1, ini))
    ano1 = ano1 + 1


if q1 == 'não' :
    if ano1 == ano3 :
        ini = ini + (ini * rf)


if ano1 == aumfinal :
    ini = ini + (ini * rf)

if q1 == 'sim' :
    ini = ini + (ini * a3)

while ano1 >= aumfinal and ano1 < anof :

    if q2 == 'sim':
        eco = eco + ((x / 100) * ini)

        if stop == 0:
            print('{} - R${}'.format(ano1, ini))
        else:
            print('{} - R${}'.format(stop, ini))

        if stop == 0:
            ano1 = ano1 + 1
        else:
            ano1 = stop + 1

        stop = ano1

        while stop != (ano1 + (r - 1)) and stop < anof:
            print('{} - R${}'.format(stop, ini))
            stop += 1

        if stop == 0:
            ini = ini + (ini * rf)
        elif stop < anof:
            ini = ini + (ini * (s * rf))

        ano1 = stop

        eco = eco + ((x / 100) * ini)
        print('{} - R${}'.format(ano1, ini))

    else :
        eco = eco + ((x / 100) * ini)
        print('{} - R${}'.format(ano1, ini))
        ano1 = ano1 + 1



if ano1 == anof :
    print('{} - R${}'.format(ano1, ini))
else :
    print('Erro!')

print(' ')

print('{}, seu salário final será R${}, com economia salva de R${}.' .format(nome, ini, eco))