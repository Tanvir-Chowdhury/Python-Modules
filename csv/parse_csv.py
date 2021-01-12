import csv

#using reader and writer module in csv
'''with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    #next(csv_reader)

    #for line in csv_reader:
    #    print(line[2])

    with open("newnames.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)'''

#using dictreader and dictwriter module in csv
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('newnames.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)