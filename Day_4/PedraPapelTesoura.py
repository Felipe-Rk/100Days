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

imagens = [pedra, papel, tesoura]

jogador = int(input("Escolha entre pedra, papel ou tesoura. Pedra = 0 / Papel = 1 / Tesoura = 2: "))
print("Você escolheu: ", imagens[jogador])

computador_escolha = random.randint(0,2)
print("O computador escolheu: ",imagens[computador_escolha])

if jogador >= 3 or jogador < 0:
    print("Você digitou errado ")

elif jogador == 0 and computador_escolha == 2: 
    print("Você ganhou!!!")

elif computador_escolha == 0 and jogador == 2:
    print("Você perdeu!!!")

elif jogador > computador_escolha:
    print("Você ganhou!!!")

elif computador_escolha > jogador:
    print("Você perdeu!!!")   

elif jogador == computador_escolha:
    print("Empate")