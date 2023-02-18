import sys


def printDetails(tableDetails):
    for i in tableDetails:
        print()
        print("Admission Number:", i)
        print("Student Name:", allStudents[i]["Name"])
        print("Module Name:", allStudents[i]["Module"])
        print("Score:", float(allStudents[i]["Score"]))
    return


def addStudent():
    print("== Add a new student==")
    print()
    a = input("Please enter the admission number: ")
    if a.lower() in [x.lower() for x in allStudents.keys()]:
        print("Admission number already exists in the system")
        a = input(
            "Please enter a new admission number  or enter 0 to return to main menu: "
        )
        if a == "0":
            return
    b = input("Please enter the student name: ")
    if not all(x.isalpha() or x.isspace() for x in b):
        print("Name should only contain alphabets!")
        return
    c = input("Please enter the module name: ")
    if not all(x.isalpha() or x.isspace() for x in c):
        print("Module name should only contain alphabets!")
        return
    try:
        d = int(input("Please enter the score: "))
    except:
        print("Score should be an integer!")
        return

    allStudents[a] = {"Name": b, "Module": c, "Score": d}
    print("Student added")
    return


def removeStudent():
    print("== Remove Student == ")
    a = input("Please enter the admission number you want to remove: ")
    if a.lower() not in [x.lower() for x in allStudents.keys()]:
        print("No such student found.")
        return
    printDetails([a])
    b = input("Is this the student you want to remove? (Yes/No): ")
    if b.lower() == "no":
        print("Student info was not removed!")
        return
    if b.lower() == "yes":
        del allStudents[a]
        print("Student info removed!")
    else:
        print("Wrong input!")
    return


def updateDetails():
    print("== Update Student == ")
    a = input("Please enter the admission number you would like to update: ")
    if a.lower() not in [x.lower() for x in allStudents.keys()]:
        print("No such student found.")
        return
    printDetails([a])
    print("Student Exist!")
    print("Enter 1 to Update Name")
    print("Enter 2 to Update Module Name")
    print("Enter 3 to Update Score")
    print("Enter 0 to return to Main Menu")
    o = int(input("What would you like to update? "))
    lst = ["Name", "Module", "Score"]
    if o == 0:
        return
    else:
        b = input(f"Enter the new {lst[o-1]}: ")
        if o == 1 or o == 2:
            if not all(x.isalpha() or x.isspace() for x in b):
                print(f"{lst[o-1]} should only contain alphabets!")
                return
        else:
            try:
                b = int(b)
            except:
                print("Score should be an integer!")
                return

        allStudents[a][lst[o - 1]] = b
        print(f"{lst[o-1]} updated!")
    return


def searchStudents():
    while True:
        print("== Search Student ==")
        print("Search By:")
        print("Enter 1 to search by Admission Number")
        print("Enter 2 to search by Module Name")
        print("Enter 3 to search by Score Range")
        print("Enter 0 to return to Main Menu")
        o = int(input("Your choice: "))
        if o == 0:
            break
        if o == 1:
            a = input("Please enter the admission number you wish to search by: ")
            if a.lower() not in [x.lower() for x in allStudents.keys()]:
                print("No student with this admission number found.")
            else:
                printDetails([a])
                print()
        elif o == 2:
            a = input("Please enter the module name you wish to search by: ")
            lst = []
            for i in allStudents.keys():
                if allStudents[i]["Module"] == a:
                    lst.append(i)
            if len(lst) == 0:
                print("No student with this module name found.")
            else:
                printDetails(lst)
                print()
        elif o == 3:
            print("Please enter the module name you wish to search by: ")
            a = int(input("Minimum Score: "))
            b = int(input("Maximum Score: "))
            lst = []
            for i in allStudents.keys():
                if a <= int(allStudents[i]["Score"]) <= b:
                    lst.append(i)
            if len(lst) == 0:
                print("No student within this range found.")
            else:
                printDetails(lst)
                print()
        else:
            print("Wrong input!")
    return


def main():
    while True:
        print()
        print("***** Welcome to SIT Mini Student Information System *****")
        print("Number of students in the system:", len(allStudents))
        print("These are the functions available:")
        print("Enter 1 to Add a new student")
        print("Enter 2 to Update an existing student info")
        print("Enter 3 to Remove an existing student info")
        print("Enter 4 to Display all student information in the system")
        print("Enter 5 to Search for student(s)")
        print("Enter -1 to Exit the application")
        print()
        option = 0
        try:
            option = int(input("Enter your Choice: "))
            print()
            if option == 1:
                addStudent()
            elif option == 2:
                updateDetails()
            elif option == 3:
                removeStudent()
            elif option == 4:
                if len(allStudents) != 0:
                    print("== Display all students ==")
                    printDetails(allStudents.keys())
                else:
                    print("There is no student information in the system!")
            elif option == 5:
                searchStudents()
            elif option == -1:
                print("Thank you for giving us a chance to serve you!")
                sys.exit()
            else:
                pass
        except ValueError:
            print("|      Invalid input!     |")


allStudents = {}


if __name__ == "__main__":
    main()