# the teacher needs to input grades
# to finish input he will write -999
# if the teacher entered grade not between 0-100 , then ignore

students_number: int = 0
sum_grades: int = 0
grade: int = 0
while True:
    grade = int(input('enter grade: '))
    if grade == -999:
        break  # jump to line18
    if grade < 0 or grade > 100:
        print('illegal grade, try again')
        continue  # jump to line8

    students_number += 1
    sum_grades += grade

avg_class: float = sum_grades / students_number
print(f"total of {students_number}, average = {avg_class:.2f}")

