#Count Vowels in a Word
#Problem:
#Write a program that takes a word from the user and counts how many vowels it has (a, e, i, o, u).
#Make sure it works for both uppercase and lowercase letters.

#🎯 Example:
#Input: Harsh

#Output: 1 (because only 'a' is a vowel)
#----------------------------------------------------------------------------------------
#code 

h=list(input("enter sentence:"))

vowel=["a","e","i","o","u"]

empty_vowel=0

for i in h:
  if i in vowel:
    empty_vewel+=1
  else:
    print("no vowel exsist.")

print(empty_vowel)
----
h=list(input("enter sentence:"))

vowel=["a","e","i","o","u"]

empty_vowel=0

for i in h:
  if i in vowel:
    empty_vowel+=1

if empty_vowel==0:
  print("no vowels")

print(f"There is {empty_vowel} vowels in the sentence")
