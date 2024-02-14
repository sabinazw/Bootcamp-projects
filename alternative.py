print(70*"=")
print("\t\t\tCONVERT YOUR SENTENCE")
print(70*"=")

sentence = input("Enter your sentence: ")

print(70*"=")

print("""
What would you like to do with your sentence? Choose option 1, 2 or 3:
* Option 1: to make each alternative character upper and lower case
* Option 2: to make each alternative word lower or upper case
* Option 3: to enter new setence
""")

option = input("Enter your option: ")

# If a user enters a option other than 1,2 or 3, program will ask to enter the option again
while not (option == "1" or option == "2" or option == "3"):
    print("Choose option 1, 2 or 3")
    option = input("Enter your option: ")

option_num = int(option)

while (option_num > 0):  

# This code makes each alternative character upper and lower case
    if option_num == 1:
        new_sentence = ""
        for index in range(len(sentence)):
            if index % 2 == 0:
                new_sentence += sentence[index].upper()
            else:
                new_sentence += sentence[index].lower()
        print(new_sentence)
        print(70*"-")

# This code makes each alternative word lower and upper case
    elif option_num == 2:
        sentence_split = sentence.split()
        sentence_list = []
        for index in range(len(sentence_split)):
            if index % 2 == 0:
                sentence_list.append(sentence_split[index].lower())
            else:
                sentence_list.append(sentence_split[index].upper())
        final_sentence = " ".join(sentence_list)
        print(final_sentence)
        print(70*"-")

# This code asks a user to enter new sentence
    elif option_num == 3:
        sentence = input("Enter new sentence: ")

# This code asks user to choose the correct option
    else:
        print("Choose option 1, 2 or 3")

    option = input("Enter your option: ")

# This code checks if the new option entry is a digit. 
# If the option entry is not a digit, the user must enter the option again
    
    while not option.isdigit():
        print("Enter numbers only! Choose option 1, 2 or 3")
        option = input("Enter your option: ")

    option_num = int(option)
    










