
#Excercise
print("Class Excercise")

#Initialize empty lists and dictionary
students_list = []
students_dict = {}

#Ask the user to input their name,age and grade
name=str(input("enter your name:"))
age=int(input("enter your age:"))
grade=int(input("enter your grade:"))

print("student information added successfully!")

# Add student information to lists and dictionary
students_list.append("John")
students_dict["John"] = {'age': age, 'grade': grade}
print(students_dict.items())


print("Student details:")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    
#search for student's name
search_name = input("Enter student name that you want to search or simply enter to skip: ")
if search_name in students_list:
    info=students_dict[search_name]
    print(f"name:{search_name}, age:{info['age']}, grade:{info['grade']}")
else:
    print("student not found!")    

#Remove the student's name
remove_name= input("enter the name that you want to remove:") 
if remove_name in students_list:
    del students_dict[remove_name]
    students_list.remove(remove_name)
    print("student removed successfully!")
else:
    print("student not found!") 