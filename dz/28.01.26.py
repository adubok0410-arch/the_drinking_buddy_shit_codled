from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int


def info(student: Student):
    print(f"{student.name}, {student.age} лет, {student.grade} класс")

def upgrade(student: Student):
    student.grade += 1
    print(f'Теперь {student.name} находится в {student.grade} классе')

def age_verification(student: Student):
    if student.age >= 18:
        return True
    else:
        return False
    
def student_comparison(student1: Student, student2: Student):
    if student1.age > student2.age:
        print(f'{student1.name} старше, чем {student2.name}')
        print()
    elif student1.age < student2.age:
        print(f'{student1.name} младше, чем {student2.name}')
        print()
    else:
        print(f'{student1.name} и {student2.name} - ровесники')
        print()

def learning_checks_in_one_class(student1: Student, student2: Student):
    if student1.grade == student2.grade:
        return True
    else:
        return False

def age_change(student: Student, year: int):
    student.age += year
    print(f"Возраст {student.name} увеличен на {year}. Теперь ему(-ей) {student.age}")
    print()

student1 = Student("Иван", 14, 3)
student2 = Student("Мария", 13, 7)

students = [student1, student2]

if learning_checks_in_one_class(student1, student2) is True:
    print(f'{student1.name} и {student2.name} учатся в одно классе.')
    print()
else:
    print(f'{student1.name} и {student2.name} не учатся в одно классе.')  
    print()

student_comparison(student1, student2)

for student in students:

    if age_verification(student) is True:
        print(f'{student.name} уже взрослый(-ая)!!!')
    else:
        print(f'{student.name} ещё ребёнок!!!')

    upgrade(student)

    age_change(student, 8)

    info(student)
    print()