import os
import csv

#Define variable for month total
vote_count = 0
#Create empty list to store vote count in 
vote_total = []
#Define variable for each vote for Kahn
vote_count_kahn = 0
#Create empty list to store each vote count for Kahn
vote_total_kahn = []
#Create variable for each vote for Correy
vote_count_correy = 0
#Create empty list to store each vote for Correy
vote_total_correy = []
#Create variable for each vote for Li
vote_count_li = 0
#Create empty list to store each vote for Li
vote_total_li = []
#Create variable for each vote for O'Tooley
vote_count_otooley = 0
#Create empty list to store votes for O'Tooley
vote_total_otooley = []
#Percentage votes for Kahn
percent_kahn_votes = 0
#Percentage votes for Correy
percent_correy_votes = 0
#Percentage votes for Li
percent_li_votes = 0
#Percentage votes for O'Tooley
percent_otooley_votes = 0

#Create path to open CSV file
csv_path = os.path.join("election_data.csv")

#Open CSV file, read it, and skip header
with open(csv_path) as election_data:

    reader = csv.reader(election_data)
    
    header = next(reader)


#Loop through reader
    for row in reader:
        #print(row)
        #Create counter to debug
        
        #count votes
        vote_count += 1
        #append to empty list
        vote_total.append(row[0])
        #print(month_count)
        #print(vote_count)

    #Creat list of candidates
    candidate_list =["Kahn","Correy","Li","O'Tooley"]


    #count votes for Kahn
    if row[2] == str("Kahn"):
        vote_count_kahn += 1
        vote_total_kahn.append(row[2])
        print(vote_count_kahn)
        percent_kahn_votes = vote_total/vote_total_kahn
        
        

    #count votes for Correy
    if row[2]  == str("Correy"):
        vote_count_correy += 1
        vote_total_correy.append(row[2])
        percent_correy_votes = vote_total/vote_total_correy

    #count votes for Li
    if row[2] == str("Li"):
        vote_count_li += 1
        vote_total_li.append(row[2])
        percent_li_votes = vote_total/vote_total_li

    #count votes for O'Tooley
    if row[2] == str("O'Tooley"):
        vote_count_otooley += 1
        vote_total_otooley.append(row[2])
        #percent_otooley_votes = int(vote_total)/int(vote_total_otooley)

#Print("Election Results")
#Print("________________")
#Print("Kahn"+percent_kahn_votes+"("+vote_total_kahn+")")
