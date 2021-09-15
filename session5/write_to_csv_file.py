import csv

with open('team.csv', 'w') as csv_file:
    header = ['Name', 'Age', 'Height']
    data = [{'Name': 'Jessica', 'Age': 23, 'Height': 172},
            {'Name': 'Trisha', 'Age': 24, 'Height': 182}
           ]

    spreadsheet = csv.DictWriter(csv_file, fieldnames=header)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)