import subprocess

#process = subprocess.Popen(['ping', '-c 4', 'python.org'], 
process = subprocess.Popen(['apt-get', 'update'], 
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            print(output.strip())
        break
        print('ERR:')
        for eoutput in process.stderr.readlines():
            print(eoutput.strip())
        break

