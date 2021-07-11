# Election_Analysis
Election results analysis using Python

## Project Overview
A Colorado Board of Elections employee has given me the folowing tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

After a successful analysis, I was asked to expand my work and check for the following information as well:
1. The voter turnout for each country
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.58

## Results
The final results were printed to the python terminal and saved into a text file.

![Screenshot (37)](https://user-images.githubusercontent.com/84139177/125204806-a511e900-e244-11eb-99cc-f52f1e134cbb.png)

#### - How many votes were cast in this congressional election?
369, 711 votes were cast in total. This information was found by creating a total vote counter first. Then, after opening the data source, a for loop was used to pass through each row and add to the total vote count.

![Screenshot (38)](https://user-images.githubusercontent.com/84139177/125204923-397c4b80-e245-11eb-86e5-161d99d5513b.png)

#### - How did each county compare between number of votes and percentage of total votes? Which county had the largest number of votes?
Denver had a substantially larger number of votes with over 82.8% of the total vote count. This information was found with a list of county names and dictionary for the county votes (both created in the same for loop that added to the total vote counter). Then, a for loop was used to calculate the vote percentage for each county. An internal if statement calculated the county with the largest amount of votes.

![Screenshot (39)](https://user-images.githubusercontent.com/84139177/125205177-962c3600-e246-11eb-9845-c25e949c1f1d.png)

#### - How did each candidate compare between number of votes and percentages of total votes? Which candidate won the election?
Diana DeGette won by a landslide with over 73% the total vote with 272,892 votes. Charles Stockham came in seond with 23.8% of the votes and Raymon Doane came in last, with only 3.1% percent. This information was found in a similar way to the county votes: a for loop was created to pull the votes out of the candidate_votes dictionary and then calculate the percentages. Then, with the votes found, a winning candidate was found in an if statement. All of the information was printed to the terminal and written to a text file, and some formatting code can be seen in the print statements. This formatting does not change the final calculations.

![Screenshot (40)](https://user-images.githubusercontent.com/84139177/125205386-9416a700-e247-11eb-991e-06843d4d3713.png)

## Summary
This script is very powerful and can be used in the future for a variety of projects. A couple projects that I would be interested in developing would be:
- Using this same data source or a similar data source that included votes by county, county preferences could be analyzed to see which areas favor certain political figures. In this case, Denver cast a very large amount of votes, and a for loop could gather how many votes in Denver where cast for each politician. If an analysis showed the majority of that population favored Diana DeGette during this election, that would be one example of why she recieved so many votes and won the election. This information can influence politicions in future elections in terms of where they focus their campaigns.
- Furthermore, this script can be expanded to include larger sets of information and even multiple data sources. Analysis could be used to track politicians throughout their campaigns over the U.S. and calculate their progress and success from state to state. Additional dictionaries can be added to include what political stances are taken and how (or if) that influences a politician's campaigns as well.
