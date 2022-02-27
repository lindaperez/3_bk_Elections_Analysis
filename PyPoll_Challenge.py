import csv
from itertools import count
import os
from collections import defaultdict

def main():

    candidates = defaultdict(int)
    county_votes = defaultdict(int) 
    #reading
    file_path = os.path.join("Resources","election_results.csv")
    total_votes = readingFile(file_path, candidates, county_votes)
    file_path = os.path.join("analysis","election_analysis.txt")
    writtingFile(file_path,candidates,county_votes, total_votes)


def writtingFile(file_path, candidates : dict, county_votes : dict, total_votes:int):

    winning_candidate = ""
    winning_county = ""
    winning_count = 0
    winning_percentage = 0
    winning_county_votes = 0
    header_summary = (
        f"\nElection Results"
        f"\n------------------------"
        f"\nTotal Votes: {total_votes:,}"
        f"\n------------------------\n"
        f"\nCounty Votes:\n")
    with open(file_path,'w') as file_analysis:
        print(header_summary)
        file_analysis.write(header_summary)
        for county in county_votes:
            county_percentage= float(county_votes[county])/float(total_votes) * 100
            if county_votes[county]>winning_county_votes:
                winning_county_votes=county_votes[county]
                winning_county = county
            county_summary = (f"{county}: {county_percentage:.1f}% ({county_votes[county]:,}) \n")
            print(county_summary, end="")
            file_analysis.write(county_summary)
        turnout_summary = (f"\n----------------------"
            f"\nLargest County Turnout: {winning_county} "
            f"\n-----------------------\n\n")
        file_analysis.write(turnout_summary)
        print(turnout_summary,end="")
        for candidate in candidates:
            votes = candidates[candidate]
            vote_percentage = float(votes)/float(total_votes) * 100
            candidate_summary=f"{candidate}: {vote_percentage:.1f}% ({votes:,}) \n"
            file_analysis.write(candidate_summary)
            print(candidate_summary)
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


def readingFile(file_path, candidates : dict,county_votes :dict): 
    total_votes = 0
    with  open(file_path,'r') as file_election:
        file_reader = csv.reader(file_election)
        next(file_reader)
        for row in file_reader:
            candidates[row[2]]+=1
            total_votes+=1
            county_votes[row[1]]+=1
    file_election.close()
    return total_votes



if __name__ == "__main__":
    main()