#Средний балл
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict={}
students = list(students)
students.sort()
grades[0]=sum(grades[0])/len(grades[0])
grades[1]=sum(grades[1])/len(grades[1])
grades[2]=sum(grades[2])/len(grades[2])
grades[3]=sum(grades[3])/len(grades[3])
grades[4]=sum(grades[4])/len(grades[4])
dict[students[0]]=grades[0]
dict[students[1]]=grades[1]
dict[students[2]]=grades[2]
dict[students[3]]=grades[3]
dict[students[4]]=grades[4]
print(dict)