file1 = open('file1.py', 'r')
data = file1.read()
file1.close()
print data

file1 = open('file2.txt', 'w')
file1.write('hello\n')
file1.write('world\n')
file1.close()
