import json

def create_and_store_data():
  """
  Creates sample data and stores it in a JSON file.
  """
  data = {
    "name": "Alice",
    "age": 25,
    "city": "Seattle",
    "hobbies": ["coding", "music", "photography"]
  }

  with open("fileRead/data.json", "w") as f:
    json.dump(data, f, indent=4)  # Add indentation for readability

def read_data():
  """
  Reads data from the JSON file and prints it.
  """
  with open("fileRead/data.json", "r") as f:
    data = json.load(f)
  print(data)
  
  print('_____Printing Hobbies_______')
  print(data["hobbies"])
  
  print('_____Printing just one hobbies_______')
  print(data["hobbies"][1])
# Create and store data
create_and_store_data()


