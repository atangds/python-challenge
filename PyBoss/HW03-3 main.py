import csv
# treat .py file as a module.
import us_state_abbrev

id = []
fName = []
lName = []
dob = []
ssn = []
state = []
with open("employee_data1.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id.append(row[0])
        name = row[1].split(" ")
        fName.append(name[0])
        lName.append(name[1])
        # split a string to a list.
        dob1 = row[2].split("-")
        # join a list to a string.
        # dob2 = "/".join(dob1)
        dob2 = f"{dob1[1]}/{dob1[2]}/{dob1[0]}"
        dob.append(dob2)
        ssn1 = row[3].split("-")
        ssn2 = "***-**-" + ssn1[2]
        ssn.append(ssn2)
        # use the variable in the module.
        # use key to look up value in a dictionary.
        state.append(us_state_abbrev.us_state_abbrev[row[4]])
newData = zip(id, fName, lName, dob, ssn, state)

with open("employee_data1_new.csv", "w", newline="") as output:
    writer = csv.writer(output)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(newData)

# repeat for another file.
id = []
fName = []
lName = []
dob = []
ssn = []
state = []
with open("employee_data2.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id.append(row[0])
        name = row[1].split(" ")
        fName.append(name[0])
        lName.append(name[1])
        dob1 = row[2].split("-")
        dob2 = f"{dob1[1]}/{dob1[2]}/{dob1[0]}"
        dob.append(dob2)
        ssn1 = row[3].split("-")
        ssn2 = "***-**-" + ssn1[2]
        ssn.append(ssn2)
        state.append(us_state_abbrev.us_state_abbrev[row[4]])
newData = zip(id, fName, lName, dob, ssn, state)

with open("employee_data2_new.csv", "w", newline="") as output:
    writer = csv.writer(output)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(newData)
