import csv

with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    # print(list(spreadsheet))
    for each_row in spreadsheet:
        print(each_row['Name'])