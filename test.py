import csv
import os
from urllib import response
import matplotlib.pyplot as plt

#current errors: stati values do not add on if file exists (side note, all stati values are multiplied by 4 for some reason, therefore I've divided by 4)

#csv format: first item is company string, second item is location string, third item is date string, fourth item is application status
new_entry = []
stati = [0, 0, 0, 0, 0]
cont = "yes"

desktop_path = os.path.expanduser('~')+'\\Desktop\\coop-application-tracker.csv'
file_exists = os.path.exists(desktop_path)

new_entry.clear()
if file_exists:
    file = open(desktop_path)
    csvreader = list(csv.reader(file))
    for row in csvreader:
        if row[3] == '1':
            stati[0] += 1
        elif row[3] == '2':
            stati[1] += 1
        elif row[3] == '3':
            stati[2] += 1
        elif row[3] == '4':
            stati[3] += 1
        elif row[3] == '5':
            stati[4] += 1
        csvreader.remove([])
    file.close()

file = open(desktop_path, 'a')

while cont == "yes":
    new_entry.clear()
    new_entry.append(input("What company did you apply to? "))
    new_entry.append(input("Where is this position located? "))
    new_entry.append(input("When did you apply here? "))
    new_entry.append(input("What is the status of your application: \t (1) Applied (2) Rejected (3) Interview (4) Offer (5) No Response \t"))
    writer = csv.writer(file)
    writer.writerow(new_entry)
    if new_entry[3] == '1':
        stati[0] += 1
    elif new_entry[3] == '2':
        stati[1] += 1
    elif new_entry[3] == '3':
        stati[2] += 1
    elif new_entry[3] == '4':
        stati[3] += 1
    elif new_entry[3] == '5':
        stati[4] += 1
    cont = input("Do you want to add another entry? \t (type 'yes' or 'no') ")
file.close()

responsevar = ["Applied", "Rejected", "Interview", "Offer", "No Response"]
fig, ax = plt.subplots()
ax.barh(responsevar, stati, color = ["blue", "Red", "cyan", "green", "black"])
plt.show()