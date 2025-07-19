#🎯Problem: Write a program that takes a word from the user and prints the word in reverse without using slicing ([::-1] is not allowed).
#
#Example:
#Input: hello

#Output: olleh
#-----------------------------------------------------------------------------
enter=input("enter your number:")
initial=""
for i in enter:
  initial=i+initial

print(initial)
#-------
#enter=input("enter your number:")

#print(enter[::-1])
