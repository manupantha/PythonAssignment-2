import csv
filename = [('name', 'address', 'age'), ('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
csvFile = open('filename.csv', 'w', newline='')
obj = csv.writer(csvFile)
for row in filename:
    obj.writerow(row)
csvFile.close()

