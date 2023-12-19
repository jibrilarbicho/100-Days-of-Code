names = ["jibril", "jemal", "abba jobir", "abbabora"]
import random

students_score = {student: random.randint(1, 100) for student in names}
print(students_score)
passed_studnet = {
    student: score for (student, score) in students_score.items() if score >= 60
}
print(passed_studnet)
