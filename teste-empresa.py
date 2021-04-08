title = 'boas vindas da empresa'
print(title.upper())

import emoji
emp = input('Qual o nome da empresa? ')
ramo = input('Qual o ramo? ')

if ramo == 'sorvete' or ramo == 'sorvetes' or ramo == 'Sorvete' or ramo == 'Sorvete' :
    emj = ':ice_cream:'
elif emp == 'nasa' or emp == 'NASA' or emp == 'Nasa' or emp == 'N.A.S.A.' :
    emj = ':earth_americas:'
else :
    emj = ':smile:'

print(emoji.emojize("Bem-vindo(a) à {} {}".format(emp.upper(), emj), use_aliases=True))