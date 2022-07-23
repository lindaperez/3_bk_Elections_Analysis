
# Election Audit Analysis Project:

Automation of reporting total results from congressional elections including senatorial and local districts. 


## Dataset

Tabulated results data source. [Election_Results.csv](https://github.com/lindaperez/elections_analysis/blob/master/Resources/election_results.csv?raw=true)

Voting Methos:
- Mail-In Ballot: Hand counted in central office.
- Punch Cards: Machine that tabulates votes totals and send results to central office.
- Direct Recording Electronic/ DRE couting machine read by a computer.

## Election-Audit questions to answer about the dataset:

- Total number of votes cast. 
- Total number of votes for each candidate. 
- The percetage of votes for each candidate. 
- The winner of the elections based on the popular vote.

## Election-Audit Results:
 
- How many votes were cast in the congressional election? Total Votes: 369,711
 
- Breakdown of the number of votes and the percentage of total votes for each county in the precinct.


    Jefferson     10.5%     38,855

    Devenr        82.8%     386,055

    Arapahoe      6.7%      24,801
 
- Which county had the largest number of votes?
 
   Denver with  386,055 votes
 
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
 
   Charles Casper Stockham    23%     85,213

   Diana DeoGette             73.8%   272,892
   
   Raymon Anthony Doane       3.1%    11,606
 
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

   Winner: Diana DeGetter 
   
   Vote Count: 272,892
   
   Percentage: 73.8%
 
## Election-Audit Summary:
 
 
This solution can be used in infinite situations, we could change the CSV file for a different file with the same
type of data (int, string, string) and do the same calculation with different valid results. We can add more rows
and transform the CSV to a bigger file.
 
 
![image](https://github.com/lindaperez/elections_analysis/blob/master/Resources/totals.png)
 
 
Next, there are two examples of possible uses of this project to generate different insights.
 
## Business Proposal #1: Presidential Elections
 
We can even calculate the presidential election of any country. First, we need that the machines that generate the
results return CSV files. We can generate the Elections Results using any number of candidates, cities, and votes.
 
### Problem: Presidential Elections
 
How to calculate the presidential elections in the US having 19,502 cities,
a population of 329.5M (Reference for the number of rows in the CSV file) and 5 candidates.
 
### Solution:
 
Create or receive a CSV file with the Ids, Cities, and candidates listed by column.
 
- Use this program if less than 1,048,576 people voted and just run it, otherwise make a refactor version.
- Refactor the code to read multiple csvs.
- Manage exceptions.
- Add a set of tests.
- Run the program and present the results.
 
With minimal changes, we can read several CSV and accumulate the results of:
   * The President for the next period
   * Cities with the highest percentage of participation
   * Cities with the highest percentage of absence
   * Other candidates results
 
### Cost: 
We need to refactor the code to manage exceptions and test if the file is greater than 1,048,576 rows.
 
## Business Proposal #2: Talent Audition
For this case Let's pretend that we need to identify the best artists and we have a list of skills.
The most skilled artist will have the highest amount of rows.

### Problem: Talent Audition
Generate the result of a talent audition having 11265 artists with 150 different types of skills.

### Solution:
The answer is easy.
- We need to fill the CSV file with the IDs of every row, the skill that the candidate has, and their name.
The list can look like this:
   * 432443,  Ability to take criticism, Linda Perez
   * 543543,  Time Managment, Zembra Carman
   * 324345,  Singer, Dorian Grace
   * 454354,  Critical Thinking, Linda Perez
   * 656878,  Self Confidence, Linda Perez
- Finally running the program we can have the most skilled artist and what are the skills most used between the artists.
 
 

