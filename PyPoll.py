import csv
import os
from collections import defaultdict

total_votes = 0
candidate_options = set()
candidates = defaultdict(int)

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#reading
file_path = os.path.join("Resources","election_results.csv")


with  open(file_path,'r') as file_election:
    file_reader = csv.reader(file_election)
    #print the header row
    headers = next(file_reader)
    for row in file_reader:
        candidates[row[2]]+=1
        total_votes+=1
        candidate_options.add(row[2])
file_election.close()

header_summary = (
    f"\nElection Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"------------------------\n")
#writting
file_path = os.path.join("analysis","election_analysis.txt")

with open(file_path,'w') as file_analysis:
    file_analysis.write(header_summary)
    for candidate in candidates:
        votes = candidates[candidate]
        vote_percentage = float(votes)/float(total_votes) * 100
        file_analysis.write(f"{candidate}: {vote_percentage:.1f}% ({votes:,}) \n")
        print(f"{candidate}: {vote_percentage:.1f}% ({candidates[candidate]:,})\n")
        if (vote_percentage>winning_percentage) and (votes>winning_count):
            winning_count = votes
            winning_percentage= vote_percentage    
            winning_candidate = candidate
  
    winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------------\n")
    print(winning_candidate_summary)
    file_analysis.write(winning_candidate_summary)
    file_analysis.close()


