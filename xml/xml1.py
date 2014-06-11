from xml.sax.saxutils import escape

file1 = open('default.content', 'r')

for line in file1:
    escaped = escape(line)
    print "%s&#xd;" % escaped.rstrip()
