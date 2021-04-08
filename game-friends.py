import random

title = 'jogo dos amigos. vamos jogar!'
print(title.upper())

p1 = input('Escolha uma pessoa: ')
p2 = input('Escolha outra pessoa: ')
p3 = input('Mais outro nome: ')
p4 = input('Tá acabando. Mais um nome: ')
p5 = input('Último nome: ')

sort = random.randint(1,5)
sort2 = random.randint(1,5)
sort3 = random.randint(1,5)
sort4 = random.randint(1,5)
sort5 = random.randint(1,5)

if sort == 1 :
    pessoa = p1
elif sort == 2 :
    pessoa = p2
elif sort == 3 :
    pessoa = p3
elif sort == 4 :
    pessoa = p4
elif sort == 5 :
    pessoa = p5

if sort2 == 1 :
    noiva = p1
elif sort2 == 2 :
    noiva = p2
elif sort2 == 3 :
    noiva = p3
elif sort2 == 4 :
    noiva = p4
elif sort2 == 5 :
    noiva = p5

if sort3 == 1 :
    morto = p1
elif sort3 == 2 :
    morto = p2
elif sort3 == 3 :
    morto = p3
elif sort3 == 4 :
    morto = p4
elif sort3 == 5 :
    morto = p5

if sort4 == 1 :
    dupla = p1
elif sort4 == 2 :
    dupla = p2
elif sort4 == 3 :
    dupla = p3
elif sort4 == 4 :
    dupla = p4
elif sort4 == 5 :
    dupla = p5


if sort5 == 1 :
    amante = p1
elif sort5 == 2 :
    amante = p2
elif sort5 == 3 :
    amante = p3
elif sort5 == 4 :
    amante = p4
elif sort5 == 5 :
    amante = p5

while pessoa == noiva or pessoa == morto or pessoa == dupla or pessoa == amante or noiva == morto or noiva == dupla or noiva == amante or morto == dupla or morto == amante or dupla == amante :
    sort = random.randint(1, 5)
    sort2 = random.randint(1, 5)
    sort3 = random.randint(1, 5)
    sort4 = random.randint(1, 5)
    sort5 = random.randint(1, 5)

    if sort == 1:
        pessoa = p1
    elif sort == 2:
        pessoa = p2
    elif sort == 3:
        pessoa = p3
    elif sort == 4:
        pessoa = p4
    elif sort == 5:
        pessoa = p5

    if sort2 == 1:
        noiva = p1
    elif sort2 == 2:
        noiva = p2
    elif sort2 == 3:
        noiva = p3
    elif sort2 == 4:
        noiva = p4
    elif sort2 == 5:
        noiva = p5

    if sort3 == 1:
        morto = p1
    elif sort3 == 2:
        morto = p2
    elif sort3 == 3:
        morto = p3
    elif sort3 == 4:
        morto = p4
    elif sort3 == 5:
        morto = p5

    if sort4 == 1:
        dupla = p1
    elif sort4 == 2:
        dupla = p2
    elif sort4 == 3:
        dupla = p3
    elif sort4 == 4:
        dupla = p4
    elif sort4 == 5:
        dupla = p5

    if sort5 == 1:
        amante = p1
    elif sort5 == 2:
        amante = p2
    elif sort5 == 3:
        amante = p3
    elif sort5 == 4:
        amante = p4
    elif sort5 == 5:
        amante = p5


print('{} vai se casar com {}, matar {}, fazer dupla sertaneja com {} e depois fugir com {}.' .format(pessoa, noiva, morto, dupla, amante))