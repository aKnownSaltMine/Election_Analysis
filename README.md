# Election_Analysis
## Project Overview
A client on the Colorado Board of Elections, in order to certify the election, hired us to perform an audit of a recent local congressional election. They wanted to know the following things:

- Calculate the total number of votes cast.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
- Get a complete list of candidates who received votes.
- The total number of votes on each candidate received.
- The percentage of votes each candidate won.
- Determine the winner of the election based on popular vote.

This was accomplished by taking the raw votes cast, utilizing [python scripting](https://github.com/aKnownSaltMine/Election_Analysis/blob/main/PyPoll_Challenge.py) to quickly read through the total votes cast to arrive at accurate count of the votes.

## Resources
- Data source: [election_results.csv](https://github.com/aKnownSaltMine/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.10.2, Visual Studio Code 1.64.2

## Summary
### Results
In this local election, there were a total of 369,711 votes. The three counties that had voters present in the election were Jefferson, Denver, and Arapahoe. Denver actually accounted for a large majority of the total votes cast with 82.8% of the total votes cast, or 306,055 numbered votes. The total county breakdown occured as followed:

| County Name | Percent of Total | Total Votes |
| :---------- | :--------------- | :---------- |
| Jefferson   | 10.5%            | 38,855      |
| Denver      | 82.8%            | 306,055     |
| Arapahoe    | 6.7%             | 24,801      |


There were also three candidates that recieved votes in this election. The candidates were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. The breakdown of the votes are as followed:

| Candidate Name          | Percent of Total | Total Votes |
| :---------------------- | :--------------- | :---------- |
| Charles Casper Stockham | 23.0%            | 85,213      |
| Diana DeGette           | 73.8%            | 272,892     |
| Raymon Anthony Doane    | 3.1%             | 11,606      |

Due to receiving the majority of the popular vote, it is clear that the election winner is Diana Degette recieving 73.8% of the total votes cast. 

The file with the official audit results can be found [here.](https://github.com/aKnownSaltMine/Election_Analysis/blob/main/analysis/election_analysis.txt)

### Audit Summary
The script created to audit this smaller election could easily be scaled to handle statewide elections for single races without even modifying the script. However, it could be adapted to also handle multiple races by including other dictionaries for each race that would be updated with each vote count and county total. Whereas now, there is only two dictionaires declared for tallying the votes like 

```
candidate_options = []
candidate_votes = {}
```

we would be able to institute a dictionary and list for each race run along the lines of:
```
c7_candidates = []
c7_votes = {}
```

Allowing for this adapatabilty would allow for more races to be counted off a single script. There is the caveat that the more races added, the longer that the script would run. However, it would be able to do it. 

Another way that we could adapt the script to scale up is for a Presidential Election, we would be able to adapt the script to have a dictionary containing the states and their electoral votes. So looping through the data, we would be able to keep track of the candidates and their votes for each state. When they would hit the majority of votes in that states, the electoral votes would be awarded to them in order to calculate the presidential winner. 