# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
student_scores = [1, 5, 6, 44, 2, 4, 5]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
heighest_score = 0
for score in student_scores:
  if score > heighest_score:
    heighest_score = score

print(heighest_score)

