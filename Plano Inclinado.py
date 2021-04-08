import math

m = float(input("Massa do corpo: "))
g = float(input("Gravidade sobre o corpo: "))
o = float(input("Ângulo do plano inclinado: "))
u = float(input("Coeficiente de atrito: "))
h = float(input("Altura do plano: "))

d = h/(math.sin(o))

if d < 0:
    d = d*(-1)
else:
    d = d

f = m*g
n = math.sin(o)/f
fat = u*n
fd = (f/math.cos(o))-fat
v = math.sqrt(2*g*h)

print("Força de deslocamento:{}; Distância a percorrer: {}; Velocidade final: {};".format(fd, d, v))
