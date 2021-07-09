#The data we need to retrieve
    # Total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

#Add our dependencies
import os
import csv

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save a file to a path
file_to_save = os.path.join("Analysis", "election_results.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate options and candidate votes
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}    

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Loop through each row in the CSV file
    for row in file_reader: 
        #Add to the total vote count
        total_votes += 1
        
        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#determine the percentage of votes for each canidate
#Iterate through the candidiate list
for candidate_name in candidate_options:
    #retrieve vote count of a canidate
    votes = candidate_votes[candidate_name]

    #calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print the candidate names, votes and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine the winning count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"---------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------------\n")

print(winning_candidate_summary)