
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

imc = round(weight / (height * height))

if imc <= 18.5:
    print(f"O imc é {imc} e esta a baixo do peso") 

elif imc <=25:
    print(f"O imc é {imc} e voce esta no peso normal")

elif imc <= 30:
    print(f"O imc é {imc} e voce esta um pouco a cima do peso")

else:
    print(f"O imc é {imc} e voce esta obeso")
