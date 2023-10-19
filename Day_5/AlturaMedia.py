# Insira uma lista Python de alturas de alunos
altura_aluno = input("Digite a altura: ").split()
for n in range (0, len (altura_aluno)):
  altura_aluno[n] = int(altura_aluno[n])
# 🚨 Não altere o código acima 👆
  
# Escreva seu código abaixo desta linha 👇


altura_total = 0
for total in altura_aluno:
  altura_total += total

print("A altura total de todos os alunos é ",altura_total)

numero_aluno = 0
for alunos in altura_aluno:
  numero_aluno +=1

print("Total de estudantes calculado ", numero_aluno)

altura_media = round(altura_total / numero_aluno)

print("A média da altura na sala é ", altura_media)






