grade =input("Введите оценки учеников: ")
m = [int (x) for x in grade.split()]
k = [i for i in m if i == 2]
print(len(k))