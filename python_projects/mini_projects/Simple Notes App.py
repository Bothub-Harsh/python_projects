#Project: Simple Notes App (Text File Notepad)
#✅ Goal: Create a Python program that lets users write, read, and append notes into a file like a personal notebook.

#🧱 Project Features:
#Write new note (overwrite the file)

#Add note (append to existing file)

#Read all notes

#Exit

#----------------------------------------------------------------------------

def write_note():
  write=input("enter your notes:")

  with open("write.txt","w") as notebook:
    notebook.write(write + "\n")
  print("note save successfully.")

def add_note():
  write=input("add note:")
  with open("write.txt","a") as edit:
    edit.write(write)
  print("note added successfully")

def read_allnotes():
  try:
    with open("write.txt","r") as show:
      show=show.read()
    print("----your notes----")
    print(show)
    print("this is your written notes.")  
  except FileNotFoundError:
    print("No notes found.please write some first.")

def main():
  while True:
      print("\n--- Notes App ---")
      print("\n1. Write new note (overwrite)")
      print("\n2. Add note (append)")
      print("\n3. Read all notes")
      print("\n4. Exit")

      try:
          enternum=int(input("\n\nEnter your number (1-4):"))
          # print(enternum)
      except ValueError:
          print("enter integer only.")  
          continue
      if enternum==1:
          write_note()

      elif enternum==2:
          add_note()

      elif enternum==3:
          read_allnotes()

      elif enternum==4:
          print("Exiting the app. Goodbye!")
          break

main()
