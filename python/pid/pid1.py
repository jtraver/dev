import os

pid1 = str(os.getpid())
print "pid1 = %s" % pid1

filename = "/tmp/" + pid1
print "filename = %s" % filename

fileh = open(filename, "w");
fileh.write(pid1)
fileh.close()

fileh = open(filename, "r");
pid2 = fileh.read()

if pid1 == pid2:
    print "success"
else:
    print "failure"
