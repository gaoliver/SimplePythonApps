title = 'descubra sobre o triângulo retângulo'
print(title.upper())

import math

cat1 = float(input('Digite o valor de um cateto: '))
cat2 = float(input('Digite o valor do outro cateto: '))
hip_quad = cat1**2 + cat2**2
hip = math.sqrt(hip_quad)

ang1 = float(input('Digite o valor de um ângulo: '))
ang2 = float(input('Digite o valor de outro ângulo: '))
angx = 180 - (ang1 + ang2)

sin = math.sin(angx)
cos = math.cos(angx)
tan = math.tan(angx)

print(' ')
# print('A Hipotenusa deste triângulo retángulo é igual a {} e o ângulo X é igual à {}, cujo seno é {}, cosseno é {} e tangente é {}.' .format(hip, angx, sin, cos, tan))
frase = 'A Hipotenusa deste triângulo retángulo é igual a {} e o ângulo X é igual à {}, cujo seno é {}, cosseno é {} e tangente é {}.'
print(frase .format(hip, angx, sin, cos, tan))