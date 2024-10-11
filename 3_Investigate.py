# File IO Python Investigate Activity - Adapted from Andy Colley (https://mrcolley.wordpress.com/) PRIMM Examples

# Task - Investigate

# Answer the questions about the code below.

def saveStudent():
  myFile = open('Students.txt','a')  #Creates/Opens Students.txt with append permissions

  print('Enter Student Details: ')
  while True:
    name = input('Student name: ') 
    line = name + '\n' 
    myFile.write(line) 

    print('Enter another student? Type quit or no to quit') 
    choice = input()

    if choice.lower() == 'no' or choice.lower() == 'quit':
      print('Goodbye!')
      break


  myFile.close()

saveStudent()

# What permissions are set when the 'students.txt' file is opened?

# Why are these permissions suitable?

# What is the purpose of the '\n' code on line 11?

# What is the purpose of the 'choice' variable?

# EXTRA RESEARCH QUESTIONS - we've not been through these coding techniques, you'll need to research to help you answer these questions.

# How does a 'while True' loop work?

# What does 'break' on line 19 do?

# Why is is suitable to use a while True loop for this scenario?

