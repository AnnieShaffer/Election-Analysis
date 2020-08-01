# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received vites
# 3. The percentage of cotes each candidate won
# 4. The total number of votes each canditate won
# 5. The winner of the election based on the votes

import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object
    print(election_data)