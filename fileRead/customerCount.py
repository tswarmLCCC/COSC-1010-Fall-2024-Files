#csvfile = open("fileRead/customers-10000.csv", "r")

with open("fileRead/customers-10000.csv", "r") as csvfile:
    # Skip the header row (assuming it exists)
    next(csvfile)

    # Read remaining data into a list of lists
    data = [row.strip().split(",") for row in csvfile]

# Count occurrences of "John" in first name column
count_john = sum(1 for row in data if row[2] == "John")

print(f"Number of people with a first name of John: {count_john}")