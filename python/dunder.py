
# http://stackoverflow.com/questions/20340815/built-in-magic-variable-names-attributes
import gc

print("\n".join(sorted({attrname for item in gc.get_objects() for attrname in dir(item) if attrname.startswith("__")})))
#>>> __about__
#>>> __abs__
#>>> __abstractmethods__
#>>> __add__
