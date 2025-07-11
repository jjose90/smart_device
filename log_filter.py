# Read the log_generator file
# Extracts and display WARNINGS and ERRORS
# Write the filtered logs to new file

def filter_logs(input_file, ouput_file=None):
    filtered = []
    with open(input_file,'r')as f:
        lines = f.readlines()
        for line in lines:
            if 'WARNING' in line or 'ERROR' in line:
                filtered.append(line)
            else:
                pass
    with open(output_file,'w') as g:
        g.writelines(filtered)
        print(f'The output file is {output_file}')

input_file = 'logfile/device_logs.txt'
output_file = 'logfile/filtered_logs.txt'
filter_logs(input_file,output_file)