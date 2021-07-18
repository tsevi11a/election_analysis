# Election Analysis

## Overview of Election Audit
This project automates the process of analyzing election results for an individual U.S. congressional precinct in Colorado. When executed, this python script reports the total number of votes cast in the election, the total number of votes for each candidate, the percentage of votes each candidate won, and the winner of the election. In addition, it also provides information regarding voter turnout for each county and determines which county had the highest turnout. 

## Resources
  * Data Source: election_results.csv
  * Software: Python 3.8.8, Visual Studio Code 1.58.2

## Election-Audit Results
This code loads the election data from a CSV file. It then iterates through each row and extracts the candidate name and county name and tallies up the votes for each candidate and county respectively. The results are then printed to the terminal and saved to a text file (see election_analysis.txt in the Analysis folder). Below is a summary of the findings from this process:
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
