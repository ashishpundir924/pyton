
list_of_students = []
list_of_age = []
list_of_country = []

i = 0
for x in range(2):
    list_of_students.append(input("Enter the Name of Student "))
    list_of_age.append(int(input("Enter the age of Student ")))
    list_of_country.append(input("Enter the country of student "))


for x, y, z in zip(list_of_students, list_of_age, list_of_country):

    print('Student Name: {0:<7} Age :{1:<2}, Nationality {2:>7}'.format(x, y, z))

