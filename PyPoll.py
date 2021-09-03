# Imports
import datetime as dt
import csv, random, os # numpy

now = dt.datetime.now()
print("The time right now is ", now)

file_path_read = os.path.join("resources", "election_results.csv")
file_path_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
winning_count = 0
winning_percentage = 0
winning_candidate = ''
candidate_opts = {}

with open(file_path_read) as election_data:
    election_data_rows = csv.reader(election_data)
    headers = next(election_data_rows)

    for row in election_data_rows:
        if row[2] not in candidate_opts.keys():
            candidate_opts[row[2]]= {'votes': 1, 'name': row[2]}
        else:
            candidate_opts[row[2]]['votes'] += 1
        total_votes += 1
print(f"Total votes: {total_votes:,}")
winning_percentage = 50
winning_count = total_votes * 0.50
for key in candidate_opts.keys():
    candidate_opts[key]['vote_percentage'] = (float(candidate_opts[key]['votes']) / float(total_votes)) * 100
    print(f"{candidate_opts[key]['name']}: received {candidate_opts[key]['vote_percentage']:.1f}% ({candidate_opts[key]['votes']:,})")
    if candidate_opts[key]['vote_percentage'] > winning_percentage and candidate_opts[key]['votes'] > winning_count:
        candidate_opts[key]['winner'] = True
        winning_candidate = candidate_opts[key]['name']
    else:
        candidate_opts[key]['winner'] = False
    
print(
    f"-------------------------\n"
    f"Winner: {candidate_opts[winning_candidate]['name']}\n"
    f"Winning Vote Count: {candidate_opts[winning_candidate]['votes']:,}\n"
    f"Winning Percentage: {candidate_opts[winning_candidate]['vote_percentage']:.1f}%\n"
    f"-------------------------\n")


# Using the with statement open the file as a text file.
with open(file_path_save, "w") as analysis_file:
    analysis_file.write('Election Results\n\n')
    analysis_file.write('Counties  in the Election\n--------------------\nArapahoe\nDenver\nJefferson')

# Close the file
analysis_file.close()