import numpy as np

name=[]
rollno=[]

def accept_details():
  enter_name=input("enter your name:")
  enter_rollno=int(input("enter your roll no:"))

  name.append(enter_name)
  rollno.append(enter_rollno)

  print("\n✅Your Data save successfully!")

def convert():
  global rollno_convert #make it assisable for use in other functions.
  rollno_convert=np.asarray(rollno)
  print("\n✅conversion list into array is done successfully!")

def analyzer():
  print("\n--analyze list--")
  print("\nType:",type(rollno_convert))
  print("\nShape:",rollno_convert.shape)
  print("\nDimension:",rollno_convert.ndim)
  print("\nData Type:",rollno_convert.dtype)
  print("\nTotal Elements:",rollno_convert.size)  
  print("\n\n✅Analyze done successfully!")

def convert_intodatatype():

  global new_variable
  new_variable=rollno_convert.astype(float)
  print("\n✅Convert to float successfully!")


def average_calculation():
  average=np.mean(new_variable)
  print("\nAverage:",average)

def harsh():
  while True:
    accept_details()
    convert()
    analyzer()
    convert_intodatatype()
    average_calculation()



harsh()  
