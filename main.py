print("Grading system")
while True:
    # input name here

    name = input("Enter your name:")
    idnum = input("Enter your id number:")
    course = input("Enter your course:")
    section = input("Enter you section:")

    # input gradees here
    quarter1 = float(input("Enter your 1st quarter grades:"))
    quarter2 = float(input("Enter your 2nd quarter grades:"))
    quarter3 = float(input("Enter your 3rd quarter grades:"))
    quarter4 = float(input("Enter your 4th quarter grades:"))

    # print results

    result = quarter1 + quarter2 + quarter3 + quarter4
    result2 = result / 4

    print(name)
    print(idnum)
    print(course)
    print(section)
    print(result2)

    another = input("Continue calculating grades of students(yes/no)?")
    if another.lower() != 'yes':
        break
