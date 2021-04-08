title = 'a cidade tem nome de santo?'
print(title.upper())

nome = input('Insira o nome da sua cidade natal: ')
res = nome.find('Santo')
res2 = nome.find('São')
res3 = nome.find('Santa')

if res >= 0 or res2 >= 0 or res3 >= 0 :
    print('Nome de Santo(a).')
else :
    print('Não é nome de Santo(a).')