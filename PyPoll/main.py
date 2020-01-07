import os
import csv

#Define variable for month total
vote_count = 0
#Create empty list to store vote count in 
vote_total = []

#Create path to open CSV file
csv_path = os.path.join("C:\\Users\\14704\\Desktop\\Python homework\\Resources\\election_data.csv")

#Open CSV file, read it, and skip header
with open(csv_path) as election_data:

    reader = csv.reader(election_data)
    
    header = next(reader)

    #key: candidate name, value: vote counts
    candidate_dictionary = {}


#Loop through reader
    for row in reader:
        #print(row)
        candidate = row[2]
        if candidate in candidate_dictionary:
            candidate_dictionary[candidate] += 1
        else: # candidate not in dict yet
            candidate_dictionary[candidate] = 1

    votes = list(candidate_dictionary.values())
    total_votes = sum(votes)
        
print('-- CAnidaates --')
print(candidate_dictionary)

print("Election Results")
print("________________")
print("Total votes:"+" "+str(total_votes))
print("________________")

winner = ''
winner_count = 0
for candidate, vote_count in candidate_dictionary.items():
    print(candidate + ": " + str(vote_count/total_votes*100) +"% ("+ str(vote_count) +")")
    if vote_count > winner_count:
        winner = candidate
        winner_count = vote_count

print("________________")
print("Winner: " + winner)
print("________________")

with open("election_results.txt","a") as f:
    print('-- CAnidaates --')
    print(candidate_dictionary)

    print("Election Results")
    print("________________")
    print("Total votes:"+" "+str(total_votes))
    print("________________")

    winner = ''
    winner_count = 0
    for candidate, vote_count in candidate_dictionary.items():
        print(candidate + ": " + str(vote_count/total_votes*100) +"% ("+ str(vote_count) +")")
        if vote_count > winner_count:
            winner = candidate
            winner_count = vote_count

    print("________________")
    print("Winner: " + winner)
    print("________________")