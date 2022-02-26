# The data we need to retrieve.
# 1. The Total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our Dependencies.
import csv
import os

# setting the file variable from relative path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initialize a total vote counter.
total_votes = 0

# Candidate list
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis
    # Read the file object with the reader fucntion.
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name for each row.
        candidate_name = row[2]

        # If the candidate is not already in the list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

print(candidate_options)