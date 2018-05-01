import csv

date = []
rev = []
with open("budget_data_1.csv") as file:
    reader = csv.reader(file)
    # skip the header row.
    next(reader)
    for row in reader:
        date.append(row[0])
        # read as string; convert to integer.
        rev.append(int(row[1]))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total Revenue: ${sum(rev)}")

revCh = []
# revenue change starts with 2nd value.
for i in range(1, len(rev)):
    revCh.append(rev[i] - rev[i-1])

print(f"Average Revenue Change: ${sum(revCh)/len(revCh)}")
# "date" list has 1 more value than "revCh" list.
print(f"Greatest Increase in Revenue: {date[revCh.index(max(revCh))+1]} ({max(revCh)})")
print(f"Greatest Decrease in Revenue: {date[revCh.index(min(revCh))+1]} ({min(revCh)})\n")

# repeat for another file.
date = []
rev = []
with open("budget_data_2.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        date.append(row[0])
        rev.append(int(row[1]))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total Revenue: ${sum(rev)}")

revCh = []
for i in range(1, len(rev)):
    revCh.append(rev[i] - rev[i-1])

print(f"Average Revenue Change: ${sum(revCh)/len(revCh)}")
print(f"Greatest Increase in Revenue: {date[revCh.index(max(revCh))+1]} ({max(revCh)})")
print(f"Greatest Decrease in Revenue: {date[revCh.index(min(revCh))+1]} ({min(revCh)})\n")
