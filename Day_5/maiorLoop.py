# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

maior_nota = student_scores[0]

for nota in student_scores: 
    if nota > maior_nota:
       maior_nota = nota

print("The highest score in the class is: ",maior_nota)



