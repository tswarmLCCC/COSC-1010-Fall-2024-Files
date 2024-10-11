# File IO Python Predict Activity - Adapted from Andy Colley (https://mrcolley.wordpress.com/) PRIMM Examples

# Task - Predict Run

# Add comments to the code to predict what it will do. 

def WriteToFile():
  
  myFile = open("Writing.txt","w") 
  myFile.write("Bob")
  myFile.close()

def AppendToFile(name):
  myFile = open("Appending.txt","a") 
  myFile.write(name + "\n")
  myFile.close()

WriteToFile()


name = "Dave"
AppendToFile(name)

name = "Freddie"
AppendToFile(name)
