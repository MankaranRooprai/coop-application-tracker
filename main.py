import csv
import os
import matplotlib.pyplot as plt

application_info = []

company = application_info.append(input("What company did you apply to? "))
location = application_info.append(input("Where is this company located? "))
date_year = application_info.append(int(input("Year: ")))
date_month = application_info.append(int(input("Month: ")))
date_day = application_info.append(int(input("Day: ")))

desktop_path = os.path.expanduser('~')+'\\Desktop\\coop-application-tracker.csv'

with open('coop-application-tracker.csv', 'w') as f:
    #create the csv writer
    writer = csv.writer(f)
    #write a row to the csv file
    writer.writerow(application_info)

status = ["Applied", "Rejected", "Interview", "Offer", "No Response"]
responses = [3, 1, 5, 7, 2]
fig, ax = plt.subplots()
ax.barh(status, responses, color = ["blue", "Red", "cyan", "green", "black"])
plt.show()