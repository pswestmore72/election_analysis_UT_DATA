# Imports
import csv, os 

file_path_read = os.path.join("resources", "election_results.csv")
file_path_write = os.path.join("analysis", "election_analysis.txt")

# Variable declarations and inits
total_votes = 0
winning_percentage = 50
winning_vote_count = 0
winning_candidate = ''
winning_county = ''
candidate_opts = {} # using dicts instead of lists to leverage their ability to store more connected data
county_opts = {}

with open(file_path_read) as election_data:
    election_data_rows = csv.reader(election_data)
    headers = next(election_data_rows)

    for row in election_data_rows:
        
        # Collecting all unique data for Counties
        if row[1] not in county_opts.keys():
            county_opts[row[1]]= {
                'votes': 1,
                'name': row[1],
                row[2]: {
                    'votes': 1,
                }
            }
        else:
            county_opts[row[1]]['votes'] += 1
        
        if row[2] not in county_opts[row[1]].keys():
            county_opts[row[1]][row[2]]= {
                'votes': 1,
                }
        else:
            county_opts[row[1]][row[2]]['votes'] += 1
        
        # Collecting all unique data for Candidates
        if row[2] not in candidate_opts.keys():
            candidate_opts[row[2]]= {
                'votes': 1,
                'name': row[2],
                }
        else:
            candidate_opts[row[2]]['votes'] += 1
        
        # Increase total vote count
        total_votes += 1

winning_vote_count = total_votes * 0.50
# Using the with statement open the file as a text file.

with open(file_path_write, "w") as analysis_file:
    analysis_file.write(f"Election Results\n-------------------------\n")
    print(f"Election Results\n-------------------------\n")
    analysis_file.write(f"Total votes: {total_votes:,}\n-------------------------\n\n")
    print(f"Total votes: {total_votes:,}\n-------------------------\n\n")

    analysis_file.write("County Votes:\n")
    print("County Votes:\n")
    winning_county_vote = 0
    for key in county_opts.keys():
        county_opts[key]['vote_percentage'] = (float(county_opts[key]['votes']) / float(total_votes)) * 100
        analysis_file.write(f"{county_opts[key]['name']}: received {county_opts[key]['vote_percentage']:.1f}% ({county_opts[key]['votes']:,})\n")
        print(f"{county_opts[key]['name']}: received {county_opts[key]['vote_percentage']:.1f}% ({county_opts[key]['votes']:,})\n")
        if county_opts[key]['votes'] > winning_county_vote:
            winning_county_vote = county_opts[key]['votes']
            winning_county = county_opts[key]['name']
    analysis_file.write("\n-------------------------\n")
    print("\n-------------------------\n")
    analysis_file.write(f"Largest County Turnout: {winning_county}\n")
    print(f"Largest County Turnout: {winning_county}\n")
    analysis_file.write("-------------------------\n\n")
    print("-------------------------\n\n")
    for key in candidate_opts.keys():
        candidate_opts[key]['vote_percentage'] = (float(candidate_opts[key]['votes']) / float(total_votes)) * 100
        analysis_file.write(f"{candidate_opts[key]['name']}: received {candidate_opts[key]['vote_percentage']:.1f}% ({candidate_opts[key]['votes']:,})\n\n")
        print(f"{candidate_opts[key]['name']}: received {candidate_opts[key]['vote_percentage']:.1f}% ({candidate_opts[key]['votes']:,})\n\n")
        if candidate_opts[key]['vote_percentage'] > winning_percentage and candidate_opts[key]['votes'] > winning_vote_count:
            candidate_opts[key]['winner'] = True
            winning_candidate = candidate_opts[key]['name']
        else:
            candidate_opts[key]['winner'] = False
    analysis_file.write("-------------------------\n")
    print("-------------------------\n")
    analysis_file.write(f"Winner: {candidate_opts[winning_candidate]['name']}\n")
    print(f"Winner: {candidate_opts[winning_candidate]['name']}\n")
    analysis_file.write(f"Winning Vote Count: {candidate_opts[winning_candidate]['votes']:,}\n")
    print(f"Winning Vote Count: {candidate_opts[winning_candidate]['votes']:,}\n")
    analysis_file.write(f"Winning Percentage: {candidate_opts[winning_candidate]['vote_percentage']:.1f}%\n-------------------------\n\n")
    print(f"Winning Percentage: {candidate_opts[winning_candidate]['vote_percentage']:.1f}%\n-------------------------\n\n")

    analysis_file.write("County vote breakdown:\n")
    print("County vote breakdown:\n")
    # County results drill down
    for county in county_opts.keys():
        analysis_file.write(f"{county} County:\n")
        print(f"{county} County:\n")
        for candidate in candidate_opts.keys():
            vote_percentage = (float(county_opts[county][candidate]['votes']) / float(county_opts[county]['votes'])) * 100
            analysis_file.write(f"{candidate}: received {vote_percentage:.1f}% of of the votes in {county} county ({county_opts[county][candidate]['votes']:,})\n")
            print(f"{candidate}: received {vote_percentage:.1f}% of of the votes in {county} county ({county_opts[county][candidate]['votes']:,})\n")
        analysis_file.write("-------------------------\n")
        print("-------------------------\n")
# Close the file
analysis_file.close()