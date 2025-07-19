#You will create a Python program where:

#The user enters the number of students.

#Then for each student, the user enters the student’s name and marks.

#The program stores all this data.

#Then it will analyze the data by:

#Showing all student names and marks

#Finding the topper (highest marks)

#Finding the lowest scorer

#Calculating average marks

#Showing a list of students who scored above 80 marks

#----------------------------------------------------------------------------------

roll_no=[]
name=[]
marks=[]

def student_details():
  enter_rollno=int(input("enter the roll no:"))
  enter_name=input("enter the number:")
  enter_marks=int(input("enter the marks:"))

  roll_no.append(enter_rollno)
  name.append(enter_name)
  marks.append(enter_marks)

  print("Your details is save successfully!")


def show_details():
  print("---Student Details---")
  for i in range(len(roll_no)):
    print(f"Roll no:{roll_no[i]} Name:{name[i]} Marks:{marks[i]}")

def topper_calculation():
  print("---Toppers---")
  for i in range(len(marks)):
    if marks[i]>=90:
      print(f"{i}.Name:{name[i]} Marks:{marks[i]}")
    else:
      print("No one is topper.4")

def lowerst_marks():
  # print("This is below")
  print("---LOSSERS---")
  for i in range(len(marks)):
    if marks[i]<=10:
      print(f"{i}.Name:{name[i]} Marks:{marks[i]}")
    else:
      print("No one is lossers.")

def average_marks_ofall_students():
  print("---This is average---")

  # marks_sum=sum(marks)
  average=sum(marks)/len(roll_no)
  print(f"Average:{average}")

def above80_students():
  print("---Above 80 Student list---")
  for i in range(len(marks)):
    if i>=80:
      print(f"{i}.Name:{name[i]} Marks:{marks[i]}")

def menu():
  while True:
    print("\n1.Fill student details.")
    print("\n2.Show student details.")
    print("\n3.Find the toppers(highest marks).")
    print("\n4.Above 80 students.")
    print("\n5.Find the lowest scores.")
    print("\n6.Calculating Average Marks.")
    print("\n7.Exit")
  

    enter=input("\nenter number(1-4):")

    if enter=="1":
      student_details()
    if enter=="2":
      show_details()
    if enter=="3":
      topper_calculation()
    if enter=="4":
      above80_students()
    if enter=="5": 
      lowerst_marks()
    if enter=="6":
      average_marks_ofall_students()
    if enter=="7":
      break


menu()