import numpy as np

marks=[]

def store_marks():
  ent=int(input("\nenter your marks:"))
  marks.append(ent)
  print("✅your marks store successfully!")

def convert_array():
  return np.array(marks)

def top_student():
  #print("---Top 3 Marks---")
  mark = convert_array()
  if len(mark)>=4:
    print("\ntop 3:",mark[[0,1,2]])
  else: 
    print("\nNot enough data for fancy indexing.")

def student_above():
  mark = convert_array()
  ha=mark[mark>=40]
  if len(ha)>0:
    print("above 40 or equal to = ",mark[mark>=40])
  else:
    print("not greater")

def menu():
  while True:
    store_marks()
    convert_array()
    top_student()
    student_above()



menu()