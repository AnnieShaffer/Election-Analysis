# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received vites
# 3. The percentage of cotes each candidate won
# 4. The total number of votes each canditate won
# 5. The winner of the election based on the votes

# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #print each row in the CSV file
    for row in file_reader:
            print(row)

with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the election")
    txt_file.write("\n-------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
