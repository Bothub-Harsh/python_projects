#Even Count Checker 🔢
#Take a list of numbers (as strings) from the user, and count how many are even.

#💡 Example:
#Input: ["2", "5", "8", "1", "6"]
#Output: 3 even numbers found.
#---------------------------------------------------------------
try:
  h=input("enter the numbers:")
  k=0
  for i in h:
    if int(i)%2==0:
      k+=1
  print(f"{k} even numbers found.")
except ValueError:
  print("Invalid input. Please enter a list of numbers.")

