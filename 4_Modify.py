# File IO Python Modify Activity - Adapted from Andy Colley (https://mrcolley.wordpress.com/) PRIMM Examples

# Task - Modify

# Modify the code so that:

# It gets input for the student's grade and passes it as a parameter into save_student 
# It concatenates the grade data to the line that is appended to the file.
# It validates the user's choice so that it only accepts 'yes' or 'no'.

def save_student():
  myFile = open('Students.txt','a')  #Creates/Opens Students.txt with append permissions

  print('Enter Student Details: ')
  while True:
    name = input('Student name: ') 
    line = name + '\n' 
    myFile.write(line) 

    print("Enter another student? Type yes to continue or no to quit") 
    choice = input()

    if choice.lower() == 'no':
      print('Goodbye!')
      break


  myFile.close()

save_student()
