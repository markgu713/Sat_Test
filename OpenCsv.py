import os

import csv

video = input("What video are you seraching for? ")
csvpath = os.path.join('..','python', 'netflix_ratings.csv')
found = False

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of "+ row[5])
            found = True
            break

    if found == False:
        print("sorry we didn't find the video")