import numpy as np

temperature=np.array([45.5 ,14.5 ,48.3 ,75.5 ,101.2 ,65.2 ,82.3 ,79.5 ,412.2 ,14.9 ,82.7 ,77.6 ,99.1])

count_high=[]
count_lower=[]

def average_temp():
  
  print("\nAverage :",np.mean(temperature))

def identify():

  for i in range(len(temperature)):
    if (temperature[i] > 37.5):
      print(f"\n{i+1}.Temperature {temperature[i]} is above 37.5°C :",temperature[i] > 37.5)

def normal():
  normal=[]
  high=[]
  for i in range(len(temperature)):
    
    if temperature[i]<=37.5:
      normal.append(i)
      
    elif temperature[i]>37.5:
      high.append(i)
  
  print(f"\nNormal count is {len(normal)} which is {temperature[temperature<=37.5]}")
  print(f"\nHigh count is {len(high)} which is {temperature[temperature>37.5]}")


def menu():
  while True:
    print("\n1.AVERAGE")
    print("\n2.IDENTIFY")
    print("\n3.COUNT")
    print("\n4.Exit")
    
    enter=input("\nenter your number (1-3):")
    
    if enter == "1":
      average_temp()
    
    elif enter == "2":
      identify()

    elif enter == "3":
      normal()

    elif enter == "4":
      break     

menu()



