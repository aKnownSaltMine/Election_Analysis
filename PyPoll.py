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
#variable to track the candidate votes
candidate_votes = {}

# Winning Canidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0.0

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

            # Tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our txt file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the txt file
    txt_file.write(election_results)
        

    # a for loop to iterate through each candidate name and calculate their total percenetage of votes
    for candidate_name in candidate_votes:
        # Grabbing the total amount of votes for each candidate
        votes = candidate_votes[candidate_name]
        # Calculating the percentage 
        vote_percentage = (float(votes) / float(total_votes)) * 100

        candidate_results = (f"{candidate_name}: recieved {vote_percentage:.1f}% ({votes:,})\n")
        # Print results to terminal
        print(candidate_results)
        # Write results to txt file
        txt_file.write(candidate_results)

        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then update the values of the winning variables
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")
    # print(winning_candidate_summary)