student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
for name,score in student_scores.items():
    if 90 < score <= 100:
        student_grades["score 91 - 100"] = "Outstanding"

    elif 80 < score <= 90:
        student_grades["score 81 - 90"] = "Exceeds Expectations"

    elif 70 < score <= 80:
        student_grades["score 71 - 80"] = "Acceptable"

    elif 60 < score <= 70:
        student_grades["score 61 - 70"] = "Not Good"

    else:
        student_grades["score 51 - 60"] = "Bad"

# 🚨 Don't change the code below 👇
print(student_grades)

