import os

print(70*"=")
print("STUDENT EXAM REGISTER")
print("Create a text file with student attendance register.")
print(70*"=")

# This function creates a student register text file
def register_form(file_name):
    students = input("Enter number of students to register for exam: ")

# This code block is used to validate the user input for the number of students
# to register for the exam. The `isdigit()` method is used to check if the input
# string consists of only digits. 
    
    while not students.isdigit():
            print("Enter numbers only!")
            students = input("Enter number of students to register for exam: ")

    number_students = int(students)
    
# The code block is responsible for creating a text file and
# writing student information into it.
    
    with open(file_name+".txt", 'a+') as file:
            file.write("STUDENT ID \tSTUDENT NAME\n\n")
    for index, student in enumerate(range(number_students), 1):
        id_number = input("Enter student ID number: ") 
        with open(file_name +".txt", 'a+') as file:
            file.write(f"{index}. {id_number} \t{15*"."}" + "\n\n")

    print(70*'-')
    print(f"The '{file_name}.txt' file has been successfully created!")
    print(70*'-')
    
# The function `check_option` prompts the user to enter an option until they
# enter either "0" or "1".
# :param option: The parameter "option" is a variable that represents the user's
# input for an option

def check_option(option):
    while not (option == "0" or option == "1"):
        print("Choose option 1 or 0")
        option = input("Enter your option: ")  

print("""
Choose  1  to create new student register.
Choose  0  to quit the program.
      """)

option = input("What would you like to do next? Choose option 1 or 0: ")

check_option(option)

# If the option is 1 we create new register file

while option == "1":

    file_name = input("Enter your file name, for example 'reg_form': ")

# This code block checks if a file with the given `file_name` already exists in
# the current directory. If the file exists, it prompts the user to enter a new
# file name. This ensures that the user does not overwrite an existing file and
# creates a unique file name for each register form.
    
    while os.path.exists(f"{file_name}.txt"):
         file_name = input(f"The '{file_name}.txt' already exists, enter new file name: ")

    register_form(file_name)
    print("Do you want to create another file? If Yes, Choose 1, to Quit Choose 0: ")
    option = input("Enter your option: ")
    check_option(option)

# If the option is 0 we quit the program
else:
    print(70*"=")
    print("\t\t\t--- Bye! ---")
    print(70*"=")




    
  
    
    

