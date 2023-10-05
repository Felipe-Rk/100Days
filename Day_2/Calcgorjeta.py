print("Calculadora de pagamentos")

valor = input("qual o valor total da conta: ")
gorjeta = input("Quanto deseja dar de gorjeta? 10% 12% 15% : ")
div = input("Sera divido em quantas pessoas: ")

new_gorjeta = (int(gorjeta) * int(valor) /100) 
total = ((new_gorjeta + int(valor)) / int(div))

total = "{:.2f}".format(total)
print(f"O valor que cada um tera que pagar é R${total}")