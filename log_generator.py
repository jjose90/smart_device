import random
import time
from datetime import datetime


devices = ['wearables','AR/VR','sensors']   # devices to simulate
log_levels = ['INFO','WARNING','ERROR'] #log levels
messages = {'wearables': {'INFO':['Heart rate normal', 'Step count updated', 'Battery at 80%'],
                          'WARNING': ['Low battery warning', 'Sensor calibration needed'],
                          'ERROR':['Heart rate sensor failure', 'Bluetooth disconnect']},
            'AR/VR':{'INFO':['Tracking stable', 'Calibration complete', 'Firmware updated'],
                      'WARNING':['Tracking jitter detected', 'Low headset battery'],
                      'ERROR':['Display failure', 'Sensor overheating']},
            'sensors':{'INFO':['LiDAR scan complete', 'GPS signal strong', 'Radar synced'],
                      'WARNING':['GPS signal weak', 'Camera lens dirty'],
                      'ERROR':['LiDAR failure', 'Radar communication lost']}} #sample messages for each log level
def sample_logs():
      device = random.choice(devices)
      levels = random.choice(log_levels)
      message = random.choice(messages[device][levels])
      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      return f'{timestamp} {device} {levels}: {message}'

def generate_logs():
   try:
     mylogs = 'logfile/device_logs.txt'
     with open (mylogs,mode = 'a') as f:
         while True:
             line = sample_logs()
             print(line)
             f.write(line+'\n')
             #f.flush()
   except:
       print("\nLog generation stopped.")
generate_logs()


