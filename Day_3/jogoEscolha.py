print('''
*******************************************************************************
                             .=.
                                "|||"
                               _.===._                            _
                            .-".'   '."-.                        (_)
                           ." ."     ". ".                    _   |   _
                           |+-+-------+-+|                  _(_)\ | /(_)_
                     +    |---+-------+---|    +           (_)---| |---(_)
                   _="=_  :|||:|_|_|_|:|||:  _="=_              |_|_|
                   |:::|  |   |  \|/  |   |  |:::|               | |
                  | ... |_|...-=) + (=-...|_| ... |              | |
        \_._._._._| ||| | o . o . o . o . o | ||| |_._._._._/    | |
        |  _   _  |  _  | _   _   _   _   _ |  _  |  _   _  |    | |
 ._._._.| |.| |.| | |.| ||.| |.| |.| |.| |.|| |.| | |.| |.| |_._.| |.
     _  |    __   |  _  |-------------------|  _  |   __    |  _ | |
    | | |   |  |  | | | | ::   .-"""-.   :: | | | |  |  |   | | || ||
    |.| |   |..|  | |.| |     | .-"-. |     | |.| |  |..|   | |.|| ||
        :         |     | .-. | |   | | .-. |     |         '    | |
                :     : |_|_|_|   |_|_|_| :     :              | |
                          _/=============\_                      | |
*******************************************************************************
''')
print("Bem vindo a Turquia")
print("Sua missão é conhecer a turquia sem ter nenhum problema") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#Write your code below this line 👇
print("Bem vindo a turquia Preste atenção nas suas escolhas e bom passeio")

print("--------------------------------------")

print("Você chegou no ponto principal da cidade e agora pode escolher se quer ir a pé ou com uma condução") 

print("---------------------------------------")

direção = input("Digite D = Direita a pé ou E = Esquerda para uma condução: ")

direção1 = direção.lower()

if direção1 == 'd' or direção1 == 'direita':

    print("\nParabens! Agora tem um rio e voce pode escolher entre atravessar nadando  ou esperar o barco \n")

    selec = input("Digite (N) para nadar ou (B) para esperar o barco: ")
    selec1 = selec.lower()
    if selec1 == "b":
            
            print("\nVocê atravessou o rio de barco e aproveitou a vista\n")
            print("Agora voce esta em duvida entre ir ao banheiro, a lanchonete ou voltar para o hotel \n")

            final = input("Escolha entre (B) para banheiro, (L) para lanchonete e (H) para voltar ao hotel: ")
            final1 = final.lower()

            if final1 == 'h':
                print("Parabéns!!! Vocês finalizou sua viagem e aproveitou tudo oque tinha de bom na cidade")

            elif final1 == 'b':
                print("Traficantes te seguiram ate o banheiro e te levaram embora para vender seus orgãos")


            else:
                print("Você pediu uma coxinha com café e quando foi pagar a conta teve um ataque cardiaco com o valor")


    else:
     print("Você entrou na aguá e pegou uma infecção e morreu")

else:
  print("Você escolheu ir com uma condução e foi sequestrado(a)...Fim de passeio")