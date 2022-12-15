'''
Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency
'''


# Number of students absent for the test

def absentS(listofstudent, numberofstudent):
    count = 0
    for i in range(numberofstudent):
        if (listofstudent[i] == 0):
            count += 1
    return count


# Maximum marks scored by the students

def MaxMarks(listofstudent,numberofstudent):
    max = 0
    for i in range(numberofstudents):
        if max<listofstudents[i]:
            max = listofstudents[i]

    return max


# Minimum marks scored by the students

def MinMarks(listofstudents,numbeofstudents):
    min = 0
    for i in range(numbeofstudents):
        if min > listofstudents[i]:
            min = listofstudents[i]

    return min


# Maximum marks frequency

def Maxfrq(listofstudents, numberofstudents):
    frq = max(listofstudents, numberofstudents)
    count = 1
    for i in range(numberofstudents):
        if frq == listofstudents[i]:
            count += 1

    return count


def Minfrq(listofstudents, numberofstudents):
    frq = min(listofstudents, numberofstudents)
    count = 1
    for i in range(numberofstudents):
        if frq == listofstudents[i]:
            count += 1

    return count


# avg marks

def avg(listofstudents, numberofstudents):
    avg = 0
    for i in range(numberofstudents):
        avg += listofstudents[i]
    avg = avg / numberofstudents
    return avg


# main function
loop = True
listofstudents = []
numberofstudents = int(input("Enter the number of students : "))
temp = 0
for i in range(numberofstudents):
    temp = int(input(f"{i} Student Marks : "))
    listofstudents.append(temp)


def showList():
    print(
        "--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n5)Enter 5 for minimum Marks Frequency\n6)Enter 6 for Count of absent student\n7) Enter 7 to create new list of marks\n8) Enter 8 to exit")


showList()

while loop:
    choice = input("Enter your Choice : ")
    if choice == "1":
        print(" The Average Marks obtained by the students is : ", avg(listofstudents, numberofstudents))
    elif choice == "2":
        print(" Maximum marks obtained by students is : ", max(listofstudents, numberofstudents))
    elif choice == "3":
        print(" Minimum marks obtained by students is : ", min(listofstudents, numberofstudents))
    elif choice == "4":
        print("Largest marks frequency : ", Maxfrq(listofstudents, numberofstudents))
    elif choice == "5":
        print("Minimum marks frequency : ", Minfrq(listofstudents, numberofstudents))
    elif choice == "6":
        print("Number of absent students are : ", absentS(listofstudents, numberofstudents))
    elif choice == "7":
        print("New list created")
        listOfStudent = []

        numberOfStudent = int(input("Enter No of Student: "))
        count = 1

        for i in range(numberOfStudent):
            marks = int(input(f"Enter marks for student {count}: "))
            listOfStudent.append(marks)
            count += 1
        print(
            "--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n5)Enter 5 for minimum Marks Frequency\n6)Enter 6 for Count of absent student\n7) Enter 7 to create new list of marks\n8) Enter 8 to exit")
    elif choice == "8":
        loop = False
    else:
        print("You entered wrong choice try again")
