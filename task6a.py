dict = {'Prince' : 22 , 'Sam' : 23 , 'Carry' : 26}
name  = input('Enter the student name :')

if (name in dict):
    print('The marks is :', dict[name])

else:
    print('student not found')