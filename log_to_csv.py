# convert your filtered logs to CSV format for easier analysis in Excel


from log_analyzer import inputfile


# 1. Take the input file
# 2. split the rows and append to another list

import csv

def log_to_csv(inputfile,outputfile):

    row = []

    with open(inputfile,mode='r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            timestamp = f'{parts[0]} {parts[1]}'
            device = parts[2]
            level,message = parts[3].split(":",1)
            message = " ".join([message]+parts[4:])
            row.append([timestamp,device,level,message])

    with open(outputfile,mode='w') as g:
        writer = csv.writer(g)
        writer.writerow(['Timestamp','Device','Level','Message'])
        writer.writerows(row)

    print(f'converted output file is {outputfile}')

inputfile = 'logfile/filtered_logs.txt'
outputfile = 'logfile/filtered_logs.csv'
log_to_csv(inputfile, outputfile)



