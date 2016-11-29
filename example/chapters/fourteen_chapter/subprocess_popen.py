from subprocess import Popen, PIPE
f = Popen(('uname', '-a'), stdout=PIPE).stdout
data =f.readline()
f.close()
print f

f = Popen('who', stdout=PIPE).stdout
data = [ eachLine.strip() for eachLine in f ]
f.close()
for eachLine in data:
    print eachLine