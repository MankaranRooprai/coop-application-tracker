import csv
import os
from urllib import response
import matplotlib.pyplot as plt

desktop_path = os.path.expanduser('~')+'\\Desktop\\coop-application-tracker.csv'

number_of_applications = []

application_info = []

stati = [0, 0, 0, 0, 0]

company = application_info.append(input("What company did you apply to? "))
location = application_info.append(input("Where is this company located? "))
date_year = application_info.append(int(input("Year: ")))
date_month = application_info.append(int(input("Month: ")))
date_day = application_info.append(int(input("Day: ")))

file_exists = os.exists(desktop_path)

if file_exists:
    file = open("co-op-application-tracker.csv")
    csvreader = csv.reader(file)
    for row in csvreader:
        number_of_applications.append(row)
        print(number_of_applications)
    
    application_info.append(next(csvreader))

status = int(input("What is the status of your application: \t (1) Applied (2) Rejected (3) Interview (4) Offer (5) No Response"))
if status == 1:
    stati[0] += 1
elif status == 2:
    stati[1] += 1
elif status == 3:
    stati[2] += 1
elif status == 4:
    stati[3] += 1
elif status == 5:
    stati[4] += 1

number_of_applications.append(application_info)

len(number_of_applications)



with open('coop-application-tracker.csv', 'a') as f:
    #create the csv writer
    writer = csv.writer(f)
    #write a row to the csv file
    writer.writerow(application_info)

responsevar = ["Applied", "Rejected", "Interview", "Offer", "No Response"]
fig, ax = plt.subplots()
ax.barh(responsevar, stati, color = ["blue", "Red", "cyan", "green", "black"])
plt.show()