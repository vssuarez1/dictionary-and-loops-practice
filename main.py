# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
print(len(students))
print(students[0]['Combo,Name'])
print(students[0]['Email'][0])
print(students[0]['Email'][1])

# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
for student in students:
    print(student['Combo,Name'])
    print(student['Email'][0])
    print(student['Email'][1])
    print("_"*25)


# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
name = input("what is you name?") 
for student in students:
    if name == student['Combo,Name']:
        print(student['Combo,Name'])
        print("this works")


# Let's try to print out the emails of the students:    


