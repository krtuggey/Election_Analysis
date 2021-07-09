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

#save the results to our text file
with open(file_to_save, "w") as txt_file:
    #After opening the file print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes = {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")

    #After printing the final vote count to the terminal save the final vote in the text file
    txt_file.write(election_results)

    #determine the percentage of votes for each candidate
    #Iterate through the candidiate list
    for candidate_name in candidate_options:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        
        #save the candidate results to the text file
        txt_file.write(candidate_results)

        #determine the winning count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #print the winning candidate's result to the terminal
    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------\n")
    print(winning_candidate_summary)

    #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)