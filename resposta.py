#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

spc = (50 * ".")
print(spc)


print("QUER SABER A RESPOSTA?")



# Inínio do Loop
start = 1
resp = []
cont = 0

while start == 1:

    # Variáveis
    print(3 * spc)

    print("Pense na pergunta para a qual você quer uma resposta.")

    print(spc)

    if resp != []:
        cont = int(input("utilizar o mesmo conjunto de respostas anteriores? Sim(1) não(2): "))

        if cont == 1:
            i = random.randint(0,N)
            respFinal = resp[i]
            print(3 * spc)
            print("Sua resposta é: {}".format(respFinal))
            

    if (resp == []) or (cont == 2):
        N = int(input("Quantas respostas existem para sua pergunta? (somente números): "))
        ask = 0

        print(spc)
        


        # Resposta SIM ou NÃO
        if N == 2:
            ask = int(input("Você precisa de 'SIM ou NÃO' como resposta? Sim(1) não(2): "))



        # Forma manual
        else:
            print(spc)
            
            for i in range(0,N):
                if i == 0:
                    resp.append(raw_input("Digite uma resposta possível: "))
                else:
                    resp.append(raw_input("Digite outra resposta possível: "))



        # SIM ou NÃO
        print(spc)

        if ask == 1:
            resp = ["Sim","Não"]
            i = random.randint(0,N)
            respFinal = resp[i]

        elif ask == 2:
            print(spc)
            
            resp = []
            for i in range(0,N):
                if i == 0:
                    resp.append(raw_input("Digite uma resposta possível: "))
                else:
                    resp.append(raw_input("Digite outra resposta possível: "))



            # Finalização
            i = random.randint(0,N)
            respFinal = resp[i]
        
            print(3 * spc)
            print("Sua resposta é: {}".format(respFinal))





    # Deseja sair?
    print(spc)

    sair = int(input("Gostaria de sair do programa? Sim(1) não(2): "))

    if sair == 1:
        exit()
    else:
        print(spc)
        start = int(input("Gostaria de recomeçar? Sim(1) não(2): "))


    

if start == 2:
    print(spc)
    print("Usuário finalizou o programa.")
