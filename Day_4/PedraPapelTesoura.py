pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

jogador = int(input("Escolha entre pedra, papel ou tesoura. Pedra = 0 / Papel = 1 / Tesoura = 2: "))

computador_escolha = random.randint(0,2)

if computador_escolha == 0:
    computador_escolha = pedra
    
elif computador_escolha == 1:
    computador_escolha = papel 

elif computador_escolha == 2:
    computador_escolha = tesoura 


if jogador == 0:
    jogador = pedra
    
elif jogador == 1:
    jogador = papel 

elif jogador == 2:
    jogador = tesoura 


if jogador == computador_escolha: 
    print("Voce escolheu", jogador)
    print("Computador escolheu", computador_escolha)
    print("EMPATE")

elif jogador == 0 and computador_escolha == 2:
    print("Você escolheu ",jogador)
    print("O computador escolheu ", computador_escolha)
    print("Você ganhou")

    if jogador == 2 and computador_escolha == 1:
        print("Você escolheu ",jogador)
        print("O computador escolheu ", computador_escolha)
        print("Você ganhou")

        if jogador == 1 and computador_escolha == 0:
            print("Você escolheu ",jogador)
            print("O computador escolheu ", computador_escolha)
            print("Você ganhou")

        else:
            print("Você escolheu ",jogador)
            print("O computador escolheu ", computador_escolha)
            print("O computador ganhou")


    else: 
        print("Você escolheu ",jogador)
        print("O computador escolheu ", computador_escolha)
        print("O computador ganhou")


else: 
    print("Você escolheu ",jogador)
    print("O computador escolheu ", computador_escolha)
    print("O computador ganhou")

    

    # pedra 0 > tesoura 2
    # tesoura 2 > papel 1
    # papel 1 > pedra 0