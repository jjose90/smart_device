#Count the total number of logs per device type (wearables, AR/VR, sensors)
#Count the total number of logs per log level (INFO, WARNING, ERROR)
#Print a clean summary report in the console

# def log_analyze(inputfile):
#     device_count = {'wearables': 0, 'AR/VR':0, 'sensors':0}
#     level_count = {'INFO':0,'WARNING':0,'ERROR':0}
#
#     with open(inputfile,mode = 'r') as f:
#         for line in f:
#             for device in device_count:
#                 if device in line:
#                  device_count[device] += 1
#             for level in level_count:
#                 if level in line:
#                  level_count[level] += 1
#
#     print('Daily Report')
#     print('Devices:')
#
#     for device,count in device_count.items():
#         print(f'{device}:{count}')
#     print('Levels:')
#     for level, count in level_count.items():
#         print(f'{level}:{count}')
#
#
# inputfile = 'logfile/device_logs.txt'
# log_analyze(inputfile)

            #OR

# from collections import Counter
#
# def log_analyze(inputfile):
#     device_count = Counter()
#     level_count = Counter()
#
#     with open(inputfile,mode='r') as f:
#         for line in f:
#             line.lower().strip()
#             try:
#               parts = line.split()
#               device = parts[2]
#               level = parts[3].replace(":","")
#               for d
#               #device_count[device] = device_count[device]+1
#               level_count[level] = level_count[level] + 1
#
#
#             except:
#               continue
#     print("Daily Reports")
#     print("\nDevices:")
#     for device,count in device_count.items():
#         print(f'{device}: {count}')
#     print("\nLevel:")
#     for level,count in level_count.items():
#         print(f'{level}: {count}')
#
# inputfile = 'logfile/device_logs.txt'
# log_analyze(inputfile)

from collections import defaultdict,Counter
def log_analyze(inputfile):
    log_data = defaultdict(Counter)
    with open(inputfile,mode='r') as f:
         for line in f:
             line.lower().strip()
             parts = line.split()
             device = parts[2]
             level = parts[3]

             log_data[device][level] = log_data[device][level]+1

    for device,levels in log_data.items():
        output = f'{device}: '+ " ".join([f'{lvl} = {count}' for lvl,count in levels.items()])
        print(output)

inputfile = 'logfile/device_logs.txt'
log_analyze(inputfile)




