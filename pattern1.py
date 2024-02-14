"""
'Star Pattern' program generates a pattern based on user input value.

"""

print(15*"=" + "STAR PATTERN" + 15*"=")

def InputCheck():
    number = input("Enter a number to create your pattern: ")
    while number.isnumeric() == False:
        print("Enter whole numbers greater than zero only!")
        number = input("Enter a number to create your pattern: ")
    return number

number = InputCheck()
rows = int(number)

while rows <= 0:
    print("Enter whole numbers greater than zero only!")
    number = InputCheck()
    rows = int(number)
    
else:
    print(42*"=")
    print()
    for row in range(1,rows+1):

# Next, we check if user input is a even or odd number, 
# then we generate the pattern
# For all rows from 1 to middle row inclusive, we add stars on each iteration
# For the remainining rows we are using slicing on each iteration
        
        if rows % 2 == 0:   # Even number of rows
            half_row = rows/2
            if row <= half_row:
                star = "*"
                row = row * star
                print(row)
            elif row > half_row: # 
                stars = rows * "*"
                index = rows - row
                print(stars[0:index+2]) 
        else:
            half_row = (rows + 1)/2 # Odd number of rows
            if row < half_row:
                star = "*"
                row = row * star
                print(row)
            elif row >= half_row:
                stars = rows * "*"
                index = (rows+1) - row
                print(stars[0:index])

    print()
    print(42*"=")

   



