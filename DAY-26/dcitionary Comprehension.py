names = ["jibril", "jemal", "abba jobir", "abbabora"]
import random

students_score = {student: random.randint(1, 100) for student in names}
print(students_score)
passed_studnet = {
    student: score for (student, score) in students_score.items() if score >= 60
}
print(passed_studnet)
sentence = "jimma shashemene asella asendabo sokkorru robe"

word = {word: len(word) for word in sentence.split(" ")}
print(word)
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {DAY: (TEMP * 9 / 5) + 32 for (DAY, TEMP) in weather_c.items()}
print(weather_f)
student_dict = {"student": ["Angella", "james", "jibril"], "score": [56, 76, 89]}
import pandas

student_DataFrames = pandas.DataFrame(student_dict)
print(student_DataFrames)
for index, row in student_DataFrames.iterrows():
    print(row)
