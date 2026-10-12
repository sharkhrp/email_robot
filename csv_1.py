import csv

name = []
project = []
email = []


with open("data.csv", "r", newline="", encoding="utf-8-sig") as file:

    reader = csv.reader(file)
    next(reader, None)
    
    for row in reader:

        	if len(row) >= 4:
                    name.append(row[2].strip())

                    project.append(row[3].strip())

                    email.append(row[4].strip())