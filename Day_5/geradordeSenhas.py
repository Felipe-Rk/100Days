
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("            Bem vindo ao gerador de senhas!!!          ")
print("--------------------------------------------------------")
nr_letras= int(input("Quantas letras você quer na sua senha?\n")) 
nr_simbolos= int(input(f"Quantos simbolos?\n"))
nr_numeros = int(input(f"Quantos numeros?\n"))
print("Anote bem sua senha em algum local seguro")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

senha =[]

for n in range(nr_letras):
    letra = random.choice(letras)
    senha.append(letra)
    #print(letra, end=" ")

for a in range(nr_simbolos):
    simbolo = random.choice(simbolos)
    senha.append(simbolo)
    #print(simbolo, end=" ")

for l in range(nr_numeros):
    numero = random.choice(numeros)
    senha.append(numero)
    #print(numero, end=" ")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(senha)
senha1 = ''.join(senha)
print(senha1)
