students_height=input("Input a list of students height").split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
    print(students_height)
    totalHeight=0
    for height in students_height:
     totalHeight +=height
    numberOfStudents=len(students_height)
    averageHeight=totalHeight/numberOfStudents
    print(averageHeight)
S