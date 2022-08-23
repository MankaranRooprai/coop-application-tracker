import csv
import os

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