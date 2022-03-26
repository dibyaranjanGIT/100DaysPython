student_heights = input("Input a list of student heights ").split(',')
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
print(sum(student_heights))

sum_height = 0
for height in student_heights:
    sum_height += height

print(sum_height)

