# Imports
import datetime as dt
import csv, random, os # numpy

now = dt.datetime.now()
print("The time right now is ", now)

file_path_read = os.path.join("resources", "election_results.csv")
file_path_save = os.path.join("analysis", "election_analysis.txt")


with open(file_path_read) as election_data:
    election_data_rows = csv.reader(election_data)
    headers = next(election_data_rows)
    print(headers)
    # Loop through looking for the video
    for row in election_data_rows:
        print(row)
        break

# Using the with statement open the file as a text file.
with open(file_path_save, "w") as analysis_file:
    analysis_file.write('Election Results\n\n')
    analysis_file.write('Counties  in the Election\n--------------------\nArapahoe\nDenver\nJefferson')

# Close the file
analysis_file.close()