# PyPoll with Python

## Overview

### Purpose
The purpose of the PyPoll with Python analysis is to assist Tom and his manager, Seth, in auditing the results of a recent election to send to the election commission.

### Background
Seth and Tom are requesting that an audit be completed on the election results and data regarding the specific counties outcomes to send to the election commission. In order to do this, we used Python to sort through the data and find the outcomes.

## Results
- How many votes were cast in this congressional election?
  - There were 369,711 total votes cast in the election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Arapahoe County had a total of **24,801 votes cast**. These votes accounted for **6.7% of the total votes** cast in the election
  - Denver County had a total of **306,055 votes cast**. These votes accounted for **82.8% of the total votes** cast in the election.
  - Jefferson County had a total of **38,885 votes cast**. These votes accounted for **10.5% of the total votes** cast in the election.
- Which county had the largest number of votes?
  - Denver county had the largest number of votes in the elections with 306,055 total votes cast.
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham recieved **85,213 total votes**. His votes account for **23.0% of the total votes** cast in the election.
  - Diana DeGette recieved **272,892 total votes**. Her votes account for **73.8% of the total votes** cast in the election.
  - Raymon Anthony Doane recieved **11,606 total votes**. His votes account for **3.1% of the total votes** cast in the election.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana Degette won the election with 272,892 votes and 73.8% of the total votes in the election.

![Election Results](https://github.com/AnnieShaffer/Election-Analysis/blob/master/Resources/Election_Results.png)

## Summary
This script can be used again with upcoming elections! The script does not specify candidate names or the counties that are being used, therefore we are able to use different data with the same script. In order to use this script again we would need to make a couple changes based on the file that is used.

Row 9 in the current script pulls the data from the location stored on this computer:
'''file_to_load = os.path.join("Resources/election_results.csv")'''
This would need to be altered to the correct path with each new set of data.