# election_analysis_utdata
election analysis for UT data class, written in python

# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election within a set of chosen counties.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number  of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: [Election Data (csv)](resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.60.0

## Summary
- Analysis Summary: [Summary (txt)](analysis/election_analysis.txt)
The analysis of the elecetion data show that:
- A total of 369,711 were cast
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The results for each candidate were:
    - Charles Casper Stockham: received 23.0% (85,213 votes)
    - Diana DeGette: received 73.8% (272,892 votes)
    - Raymon Anthony Doane: received 3.1% (11,606 votes)
- The winning candidate was:
    - Diana DeGette, who received 73.8% of the total vote (272,892 votes).

#### Election-Audit Summary
This script can be augmented further to give a deeper look into the performance of candidates within each county. As well as expanded upon, with an expanded dataset, to show more information regarding the caster of each ballot and how their demographics may or may not show trends for certain candidates.
