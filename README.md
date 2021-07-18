# Election Analysis

## Overview of Election Audit
This project automates the process of analyzing election results for an individual congressional precinct in Colorado. When executed, this python script reports the total number of votes cast in the election, the total number of votes for each candidate, the percentage of votes each candidate won, and the winner of the election. In addition, it also provides information regarding voter turnout for each county and determines which county had the highest turnout.

## Resources
  * Data Source: election_results.csv
  * Software: Python 3.8.8, Visual Studio Code 1.58.2

## Election-Audit Results
The complete python script can be found [here](PyPoll_Challenge.py).

In short, this code loads the election data from a CSV file which contains a table listing the ballot ID, where it was cast (i.e. the county), and the candidate that was voted for. The code then iterates through each row and extracts the county name and candidate name and tallies up the number of votes in each county and the total votes for each candidate. The results are then printed to the terminal and saved to a text file [(election_results.txt)](Analysis/election_results.txt). 

### Summary of Results

  * There were a total of 369,711 votes cast in this election.
  
  * **County Results:**
      * Jefferson: 10.5% (38,855 votes)
      * Denver: 82.8% (306,055 votes)
      * Arapahoe: 6.7% (24,801 votes)
  
      * The county which had the largest number of votes was Denver.
  
  * **Candidate Results:**
      * Charles Casper Stockham received 85,213 votes which is 23.0% of total votes
      * Diana DeGette received 272,892 votes which is 73.8% of total votes
      * Raymon Anthony Doane received 11,606 votes which is 3.1% of total votes 
  
      * The winner of the election was Diana DeGette who won 73.8% of the total votes. 

## Election-Audit Summary
The advantage of having this script to automate the audit process is that it can then be used to audit other elections (e.g. elections in other precincts). For example, by simply modifying the file to load (highlighted below), we can run the same code and quickly get the results for different precincts (assuming that the election data for other precincts is presented in the same tabular format).
```json
file_to_load = os.path.join("Resources", "election_results.csv")
```
Even if the data is arranged differently, we can do a simple modification to extract the data from the appropriate column within the new dataset. Below is a copy of the current code which uses specific indexes to find the candidate name and county name. If this information is positioned in a different column within the new dataset, we can amend the highlighted indexes below to reference the correct column in the dataset.
```json
    # Get the candidate name from each row.
        candidate_name = row[2]

    # Extract the county name from each row.
        county_name = row[1]
```
With these small modifications, this code can easily be adapted to automate the audit for several other elections, thus creating efficiencies and improving reliability. 
