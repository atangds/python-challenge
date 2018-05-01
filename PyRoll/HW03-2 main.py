import csv

voter = []
voteFor = []
with open("election_data_1.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        voter.append(row[0])
        voteFor.append(row[2])

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(voter)}")
print("-------------------------")

# get a list of distinct values of candidates in alphabetic order.
cands = list(set(voteFor))
cands.sort()
# get a vote count for each candidate.
candVotes = []
for cand in cands:
    candVotes.append(voteFor.count(cand))

for i in range(len(cands)):
    print(f"{cands[i]}: {'{:.2%}'.format(candVotes[i]/len(voteFor))} ({candVotes[i]})")
print("-------------------------")
print(f"Winner: {cands[candVotes.index(max(candVotes))]}")
print("-------------------------\n")

# repeat for another file.
voter = []
voteFor = []
with open("election_data_2.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        voter.append(row[0])
        voteFor.append(row[2])

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(voter)}")
print("-------------------------")

cands = list(set(voteFor))
cands.sort()
candVotes = []
for cand in cands:
    candVotes.append(voteFor.count(cand))

for i in range(len(cands)):
    print(f"{cands[i]}: {'{:.2%}'.format(candVotes[i]/len(voteFor))} ({candVotes[i]})")
print("-------------------------")
print(f"Winner: {cands[candVotes.index(max(candVotes))]}")
print("-------------------------\n")
