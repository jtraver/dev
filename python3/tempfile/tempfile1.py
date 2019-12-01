#!/usr/bin/env python3
#!/usr/bin/python

import tempfile
import os

tmp1 = tempfile.NamedTemporaryFile()
print("tmp1 = %s" % str(tmp1))
print("tmp1 = %s" % dir(tmp1))
print("tmp1.name = %s" % str(tmp1.name))

tmp1 = tempfile.NamedTemporaryFile(suffix='.sql')
print("tmp1 = %s" % str(tmp1))
print("tmp1 = %s" % dir(tmp1))
print("tmp1.name = %s" % str(tmp1.name))

tmp1 = tempfile.NamedTemporaryFile(suffix='.sql', prefix='ldt_scan')
print("tmp1 = %s" % str(tmp1))
print("tmp1 = %s" % dir(tmp1))
print("tmp1.name = %s" % str(tmp1.name))

os.system("ls " + tmp1.name)

tmp1.close()

tmp1 = tempfile.NamedTemporaryFile(suffix='.sql', prefix='ldt_scan')
print("tmp1 = %s" % str(tmp1))
print("tmp1 = %s" % dir(tmp1))
print("tmp1.name = %s" % str(tmp1.name))

os.system("ls " + tmp1.name)

tmp1.close()


def write_command_to_file(file_name, command):
    tmp1 = tempfile.NamedTemporaryFile(suffix='.txt', prefix=file_name)
    # print "write_command_to_file: file_name = %s" % str(tmp1.name) # pass in a verbose flag
    # print "write_command_to_file: command = %s" % str(command)
    text_file = tmp1.file
    text_file.write(command)
    text_file.close()
    return tmp1

tmp2 = write_command_to_file('test1', 'test2\n')
os.system("ls " + tmp2.name)
os.system("cat " + tmp2.name)
os.system("ls " + tmp2.name)
tmp2.file.close()
os.system("ls " + tmp2.name)
os.system("cat " + tmp2.name)
os.system("ls " + tmp2.name)
tmp2.close()
os.system("ls " + tmp2.name)
os.system("echo cat " + tmp2.name)
os.system("cat " + tmp2.name)
os.system("ls " + tmp2.name)

tmp2 = write_command_to_file('test3', 'test4\n')
os.system("echo ls " + tmp2.name)
os.system("ls " + tmp2.name)
os.system("echo cat " + tmp2.name)
os.system("cat " + tmp2.name)
os.system("echo ls " + tmp2.name)
os.system("ls " + tmp2.name)
print("tmp2.name = %s" % str(tmp2.name))
