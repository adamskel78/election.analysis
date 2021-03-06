# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Set total vote count to zero
total_votes = 0

# Create candidate list
candidate_options = []

# Declare an empty dictaionary
candidate_votes = {}

#Declare a variable for the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

    # IF the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

        #Create candidate key
            candidate_votes[candidate_name] = 0

        #Add one vote for everytime a candidate appears in row
        candidate_votes[candidate_name] += 1

    # save results to our text file
with open(file_to_save, "w") as txt_file:
        
        #Print the final vote count to the terminal.
    election_results= (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"\nTotal Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

# 3. The total number of votes cast


# 2. A complete list of candidates who recieved votes


# 3. The percentage of votes each candidate won
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print vote percentage
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #Saver results to txt file
        txt_file.write(candidate_results)


# Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  

# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    
    # 5. The winner of the election based on popular vote
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)



    # Print each candidate, their voter count, and percentage to the terminal.
    txt_file.write(winning_candidate_summary)