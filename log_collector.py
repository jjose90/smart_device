#watch device_log file and prints new log lines as they appear on the console
# especially the ones with WARNING or ERROR.
import os
import time


def collector(inputfile):
 try:
    with open(inputfile,mode='r') as f:
        f.seek(0,os.SEEK_END)
        while True:
           line = f.readline()
           if not line:
               time.sleep(0.5)
           elif 'WARNING' in line or 'ERROR' in line:
                   print(f'The lines are {line}')
 except:
   print("\nLog generation stopped.")

inputfile = 'logfile/device_logs.txt'
collector(inputfile)