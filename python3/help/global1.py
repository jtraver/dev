#!/usr/bin/env python3
#!/usr/bin/python


import apihelper

# apihelper.info(set1)

print(("%s" % str(dir())))
print(("%s" % str(dir(__builtins__))))
apihelper.info(__builtins__)
print(("%s" % str(dir(__doc__))))

for item1 in dir():
    print(("%s" % item1))

# __builtins__
# __doc__
# __file__
# __name__
# __package__
# apihelper

print(("__builtins__ = %s" % str(__builtins__)))
print(("__builtins__ = %s" % str(type(__builtins__))))
for item1 in dir(__builtins__):
    print(("__builtins__.%s" % item1))

print(("__doc__ = %s" % str(__doc__)))
print(("__doc__ = %s" % str(type(__doc__))))
for item1 in dir(__doc__):
    print(("__doc__.%s" % item1))

print(("__file__ = %s" % str(__file__)))
print(("__file__ = %s" % str(type(__file__))))
for item1 in dir(__file__):
    print(("__file__.%s" % item1))

print(("__name__ = %s" % str(__name__)))
print(("__name__ = %s" % str(type(__name__))))
for item1 in dir(__name__):
    print(("__name__.%s" % item1))

print(("__package__ = %s" % str(__package__)))
print(("__package__ = %s" % str(type(__package__))))
for item1 in dir(__package__):
    print(("__package__.%s" % item1))

print(("apihelper = %s" % str(apihelper)))
print(("apihelper = %s" % str(type(apihelper))))
for item1 in dir(apihelper):
    print(("apihelper.%s" % item1))
