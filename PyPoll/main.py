import os
import csv

# call csv file
election_data_csv = os.path.join(r"C:\Users\Lori Bissell\OneDrive\Documents\Data Analytics Bootcamp\python-challenge\Starter_Code\PyPoll\Resources\election_data.csv")

#Set up variables to store counts
num_voters = 0
num_candidates = set()
candidate_votes = {}

# open csv file
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    row = next(csv_reader)
  
    # identify the column from csv we want to pull info from
    candidate_names = row[2]
    
    for row in csv_reader:
        # count the number of voters
        num_voters = num_voters + 1
        # identify the row with candidate names
        candidates = row[2].split(",")
        # create list of different names in candidate list
        num_candidates.update(c.strip()for c in candidates)
        different_candidates = len(num_candidates)
        names_of_candidates = list(num_candidates)
 
        # calculate number of votes per candidate
        if candidates[0] in candidate_votes.keys():
            
            candidate_votes[candidates[0]] += 1
        else:
            candidate_votes[candidates[0]] = 1
        # identify winners with max
        winner = max(candidate_votes.values())
        name_of_winner = list(candidate_votes.keys())[list(candidate_votes.values()).index(winner)]
        
    print("Election Results")
    print("-------------------------------------------\n")
    print(f"Total Votes: {num_voters}") #369711
    print("-------------------------------------------\n")
    print(f"{(list(candidate_votes.keys())[0])}: {(round((list(candidate_votes.values())[0]) / (num_voters)*100,3))}% ({list(candidate_votes.values())[0]})\n")
    print(f"{(list(candidate_votes.keys())[1])}: {(round((list(candidate_votes.values())[1]) / (num_voters)*100,3))}% ({list(candidate_votes.values())[1]})\n")
    print(f"{(list(candidate_votes.keys())[2])}: {(round((list(candidate_votes.values())[2]) / (num_voters)*100,3))}% ({list(candidate_votes.values())[2]})\n")
    print("-------------------------------------------\n")
    print(f"Winner: {name_of_winner}")
    #print(different_candidates) #3
    #print(names_of_candidates) #Diana, Raymon, Charles
    #print(candidate_votes) #charles:85213
    #print(list(candidate_votes.keys())[0]) #Charles Casper Sockham
    #print(list(candidate_votes.keys())[1]) #Diana DeGette
    #print(list(candidate_votes.keys())[2]) #Raymon Anthony Doane
    #print(list(candidate_votes.values())[0]) #85213
    #print(list(candidate_votes.values())[1]) #272892
    #print(list(candidate_votes.values())[2]) #11606
    #print(round((list(candidate_votes.values())[0]) / (num_voters)*100,3)) #23.049
    #print(round((list(candidate_votes.values())[1]) / (num_voters)*100,3)) #73.812
    #print(round((list(candidate_votes.values())[2]) / (num_voters)*100,3)) #3.139
    #print(winner)
    #print(name_of_winner)

# write txt file    
with open("PyPoll/Analysis/pypoll_result.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------------------------\n")
    txt_file.write(f"Total votes: {num_voters}\n")
    txt_file.write("-------------------------------------------\n")
    txt_file.write(f"{(list(candidate_votes.keys())[0])}: {(round((list(candidate_votes.values())[0]) / (num_voters)*100,3))}% ({list(candidate_votes.values())[0]})\n")
    txt_file.write(f"{(list(candidate_votes.keys())[1])}: {(round((list(candidate_votes.values())[1]) / (num_voters)*100,3))}% ({list(candidate_votes.values())[1]})\n")
    txt_file.write(f"{(list(candidate_votes.keys())[2])}: {(round((list(candidate_votes.values())[2]) / (num_voters)*100,3))}% ({list(candidate_votes.values())[2]})\n")
    txt_file.write("-------------------------------------------\n")
    txt_file.write(f"Winner: {name_of_winner}\n")
    txt_file.write("-------------------------------------------\n")