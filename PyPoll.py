import csv
from itertools import count
import os
from collections import defaultdict

total_votes = 0
candidate_options = set()
candidates = defaultdict(int)
county_votes = defaultdict(int)

winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
winning_county_votes = 0
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
        county_votes[row[1]]+=1
file_election.close()

header_summary = (
    f"\nElection Results\n"
    f"\n------------------------"
    f"\nTotal Votes: {total_votes:,}"
    f"\n------------------------\n"
    f"\nCounty Votes:")
print(header_summary)
#writting
file_path = os.path.join("analysis","election_analysis.txt")

with open(file_path,'w') as file_analysis:
    file_analysis.write(header_summary)
    
    for county in county_votes:
        county_percentage= float(county_votes[county])/float(total_votes) * 100
        if county_votes[county]>winning_county_votes:
            winning_county_votes=county_votes[county]
            winning_county = county
        print(f"{county}: {county_percentage:.1f}% ({county_votes[county]:,})")
        file_analysis.write(f"{county}: {county_percentage:.1f}% ({county_votes[county]:,}) \n")
    turnout_summary = (f"\n----------------------"
        f"\nLargest County Turnout: {winning_county} "
        f"\n-----------------------\n")
    file_analysis.write(turnout_summary)
    print(turnout_summary)
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


