import numpy as np

marks = np.array([
    [88, 76, 92, 85],  
    [45, 67, 56, 70],  
    [92, 95, 91, 90],  
    [35, 42, 40, 38],  
    [60, 72, 65, 68]   
])

store_total=[] 
hig=[]

def sum():
  for i in range(len(marks)):
      total=np.sum(marks[i])
      store_total.append(total)
  
#calculate average marks per subject
def average_score():  
  for i in range(len(store_total)):
    print(f"Student {i+1} average marks :{np.mean(marks[i])}")

#highest total marks 
def highest_total():
  for i in range(len(store_total)):
    if store_total[i] >= 90:
      hig.append(store_total[i])

  print(f"Highest total marks :{np.array(hig)}")

#student pass above 50 average
def above():
  for i in range(len(store_total)):
    if store_total[i]>=50:
      print(f"Student {i} passed")
    else:
      print(f"Student {i} failed")



def menu():
  while True:
    sum()
    print("\n1.AVERAGE MARKS STUDENTS")
    print("\n2 HIGHEST TOTAL MARKS")
    print("\n3.STUDENTS PASS ABOVE 50 AVERAGE")
    print("\n4.Exit")

    enter=input("\nenter your number (1-3):")

    if enter == "1":
      average_score()

    elif enter == "2":
      highest_total()

    elif enter == "3":
      above()

    elif enter == "4":
      break     

menu()