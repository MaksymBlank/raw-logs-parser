import csv

CSV_INPUT = 'logs.csv'
CSV_OUTPUT = 'logs_report.csv'

tempCSV = {}
ips = {}


with open(CSV_INPUT, 'r') as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
        url = row[14] # URL field
        ip = row[3] # Client IP field

        if url in tempCSV:
            tempCSV[url][16] += 1 # Summarize 'Hits' values
            tempCSV[url][8] = int(tempCSV[url][8]) + int(row[8]) # Summarize 'Client-to-Server' values
            tempCSV[url][9] = int(tempCSV[url][9]) + int(row[9]) # Summarize 'Server-to-Client' values
            tempCSV[url][11] = float(tempCSV[url][11]) + float(row[11]) # Summarize 'TimeTaken' values

            # adding IP to cache and as a visitor
            if url in ips:
                if ip not in ips[url]:
                    ips[url].append(ip)
                    tempCSV[url][17] += 1  # Summarize 'Visitors' values
        else:
            row.append(1)
            row.append(1)

            ips[url] = []
            ips[url].append(ip)

            tempCSV[url] = row
csvFile.close()

with open(CSV_OUTPUT, 'a') as csvOutputFile:
    writer = csv.writer(csvOutputFile)

    for key in tempCSV:
        writer.writerow(tempCSV[key])

csvOutputFile.close()