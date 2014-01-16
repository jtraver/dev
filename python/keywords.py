import keyword
import apihelper

print type(keyword)

print dir(keyword)

print keyword.kwlist

apihelper.info(keyword)

# ['__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'iskeyword', 'kwlist', 'main']

print "\nSECTION API HELPER"
print "\nkeyword.__all__"
apihelper.info(keyword.__all__)

print "\nkeyword.__builtins__"
apihelper.info(keyword.__builtins__)

print "\nkeyword.__doc__"
apihelper.info(keyword.__doc__)

print "\nkeyword.__file__"
apihelper.info(keyword.__file__)

print "\nkeyword.__name__"
apihelper.info(keyword.__name__)

print "\nkeyword.__package__"
apihelper.info(keyword.__package__)

print "\nkeyword.iskeyword"
apihelper.info(keyword.iskeyword)

print "\nkeyword.kwlist"
apihelper.info(keyword.kwlist)

print "\nkeyword.main"
apihelper.info(keyword.main)

print "\nSECTION TYPE"
print "\nkeyword.__all__"
print type(keyword.__all__)
print keyword.__all__

print "\nkeyword.__builtins__"
print type(keyword.__builtins__)
print keyword.__builtins__

print "\nkeyword.__doc__"
print type(keyword.__doc__)
print keyword.__doc__

print "\nkeyword.__file__"
print type(keyword.__file__)
print keyword.__file__

print "\nkeyword.__name__"
print type(keyword.__name__)
print keyword.__name__

print "\nkeyword.__package__"
print type(keyword.__package__)
print keyword.__package__

print "\nkeyword.iskeyword"
print type(keyword.iskeyword)
print keyword.iskeyword
print keyword.iskeyword("in")
print keyword.iskeyword("out")

print "\nkeyword.kwlist"
print type(keyword.kwlist)
print keyword.kwlist

print "\nkeyword.main"
print type(keyword.main)
print keyword.main
# the main to call when trying to generate the keywords file for the python library, probably as input to kwlist
# print keyword.main()

print "\nSECTION DIR"
print "\nkeyword.__all__"
print dir(keyword.__all__)

print "\nkeyword.__builtins__"
print dir(keyword.__builtins__)

print "\nkeyword.__doc__"
print dir(keyword.__doc__)

print "\nkeyword.__file__"
print dir(keyword.__file__)

print "\nkeyword.__name__"
print dir(keyword.__name__)

print "\nkeyword.__package__"
print dir(keyword.__package__)

print "\nkeyword.iskeyword"
print dir(keyword.iskeyword)

print "\nkeyword.kwlist"
print dir(keyword.kwlist)

print "\nkeyword.main"
print dir(keyword.main)
