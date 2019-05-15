import csv
import gzip
import os

CSV_OUTPUT = 'logs.csv'
LOGS_INPUT_FOLDER = './data.example' # change to ./data

logs = []

# Add names of all .gz files to list
# r=root, d=directories, f = files
for r, d, f in os.walk(LOGS_INPUT_FOLDER):
    for file in f:
        if '.log.gz' in file:
            logs.append(os.path.join(r, file))

# Gets data from every single log and appends it in the .csv file
with open(CSV_OUTPUT, 'a') as fileCSV:
    writer = csv.writer(fileCSV)

    i = 0
    for log in logs:
        i += 1
        print(i, '/', len(logs))
        with gzip.open(log, 'rt') as file:
            tempLog = {}
            for line in file:
                if not line.startswith('#'):
                    fields = line.split('	')
                    fields.pop()

                    if(len(fields) > 1):
                        # Searches in tempLog for the request URL
                        if fields[5] in tempLog:
                            tempLog[fields[5]][8] = int(tempLog[fields[5]][8]) + int(fields[8]) # Summarize 'Client to Server' values
                            tempLog[fields[5]][9] = int(tempLog[fields[5]][9]) + int(fields[9]) # Summarize 'Server to Client' values
                            tempLog[fields[5]][11] = float(tempLog[fields[5]][11]) + float(fields[11])  # Summarize 'Time Taken' values
                        else:
                            tempLog[fields[5]] = fields

            for key, log in tempLog.items():
                writer.writerow(log)
        file.close()

fileCSV.close()