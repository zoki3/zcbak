import subprocess

#process = subprocess.Popen(['echo', 'More output'],
process = subprocess.Popen(['apt-get', 'update'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE,
                     universal_newlines=True)
stdout, stderr = process.communicate()

print('stdout:',stdout)
print('stderr:',stderr)
