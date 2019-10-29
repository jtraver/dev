#!/usr/bin/env python3
#!/usr/bin/python
# 
import apihelper
# 
print "str = %s" % str(str)
# 
# str = <type 'str'>
print "str = %s" % str(dir(str))
# str = ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
apihelper.info(str)
# 
# __add__   
#     x.__add__(y) <==> x+y
# 
# __class__ 
#     type(object) -> the object's type type(name, bases, dict) -> a new type
# 
# __contains__
#     x.__contains__(y) <==> y in x
# 
# __delattr__
#     x.__delattr__('name') <==> del x.name
# 
# __eq__    
#     x.__eq__(y) <==> x==y
# 
# __format__
#     S.__format__(format_spec) -> string Return a formatted version of S as described by format_spec.
# 
# __ge__    
#     x.__ge__(y) <==> x>=y
# 
# __getattribute__
#     x.__getattribute__('name') <==> x.name
# 
# __getitem__
#     x.__getitem__(y) <==> x[y]
# 
# __getnewargs__
#     None
# 
# __getslice__
#     x.__getslice__(i, j) <==> x[i:j] Use of negative indices is not supported.
# 
# __gt__    
#     x.__gt__(y) <==> x>y
# 
# __hash__  
#     x.__hash__() <==> hash(x)
# 
# __init__  
#     x.__init__(...) initializes x; see help(type(x)) for signature
# 
# __le__    
#     x.__le__(y) <==> x<=y
# 
# __len__   
#     x.__len__() <==> len(x)
# 
# __lt__    
#     x.__lt__(y) <==> x<y
# 
# __mod__   
#     x.__mod__(y) <==> x%y
# 
# __mul__   
#     x.__mul__(n) <==> x*n
# 
# __ne__    
#     x.__ne__(y) <==> x!=y
# 
# __new__   
#     T.__new__(S, ...) -> a new object with type S, a subtype of T
# 
# __reduce__
#     helper for pickle
# 
# __reduce_ex__
#     helper for pickle
# 
# __repr__  
#     x.__repr__() <==> repr(x)
# 
# __rmod__  
#     x.__rmod__(y) <==> y%x
# 
# __rmul__  
#     x.__rmul__(n) <==> n*x
# 
# __setattr__
#     x.__setattr__('name', value) <==> x.name = value
# 
# __sizeof__
#     S.__sizeof__() -> size of S in memory, in bytes
# 
# __str__   
#     x.__str__() <==> str(x)
# 
# __subclasshook__
#     Abstract classes can override this to customize issubclass(). This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).
# 
# _formatter_field_name_split
#     None
# 
# _formatter_parser
#     None
# 
# capitalize
#     S.capitalize() -> string Return a copy of the string S with only its first character capitalized.
# 
# center    
#     S.center(width[, fillchar]) -> string Return S centered in a string of length width. Padding is done using the specified fill character (default is a space)
# 
# count     
#     S.count(sub[, start[, end]]) -> int Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.
# 
# decode    
#     S.decode([encoding[,errors]]) -> object Decodes S using the codec registered for encoding. encoding defaults to the default encoding. errors may be given to set a different error handling scheme. Default is 'strict' meaning that encoding errors raise a UnicodeDecodeError. Other possible values are 'ignore' and 'replace' as well as any other name registered with codecs.register_error that is able to handle UnicodeDecodeErrors.
# 
# encode    
#     S.encode([encoding[,errors]]) -> object Encodes S using the codec registered for encoding. encoding defaults to the default encoding. errors may be given to set a different error handling scheme. Default is 'strict' meaning that encoding errors raise a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and 'xmlcharrefreplace' as well as any other name registered with codecs.register_error that is able to handle UnicodeEncodeErrors.
# 
# endswith  
#     S.endswith(suffix[, start[, end]]) -> bool Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.
# 
# expandtabs
#     S.expandtabs([tabsize]) -> string Return a copy of S where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.
# 
# find      
#     S.find(sub [,start [,end]]) -> int Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
# 
# format    
#     S.format(*args, **kwargs) -> string Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').
# 
# index     
#     S.index(sub [,start [,end]]) -> int Like S.find() but raise ValueError when the substring is not found.
# 
# isalnum   
#     S.isalnum() -> bool Return True if all characters in S are alphanumeric and there is at least one character in S, False otherwise.
# 
# isalpha   
#     S.isalpha() -> bool Return True if all characters in S are alphabetic and there is at least one character in S, False otherwise.
# 
# isdigit   
#     S.isdigit() -> bool Return True if all characters in S are digits and there is at least one character in S, False otherwise.
# 
# islower   
#     S.islower() -> bool Return True if all cased characters in S are lowercase and there is at least one cased character in S, False otherwise.
# 
# isspace   
#     S.isspace() -> bool Return True if all characters in S are whitespace and there is at least one character in S, False otherwise.
# 
# istitle   
#     S.istitle() -> bool Return True if S is a titlecased string and there is at least one character in S, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.
# 
# isupper   
#     S.isupper() -> bool Return True if all cased characters in S are uppercase and there is at least one cased character in S, False otherwise.
# 
# join      
#     S.join(iterable) -> string Return a string which is the concatenation of the strings in the iterable. The separator between elements is S.
# 
# ljust     
#     S.ljust(width[, fillchar]) -> string Return S left-justified in a string of length width. Padding is done using the specified fill character (default is a space).
# 
# lower     
#     S.lower() -> string Return a copy of the string S converted to lowercase.
# 
# lstrip    
#     S.lstrip([chars]) -> string or unicode Return a copy of the string S with leading whitespace removed. If chars is given and not None, remove characters in chars instead. If chars is unicode, S will be converted to unicode before stripping
# 
# partition 
#     S.partition(sep) -> (head, sep, tail) Search for the separator sep in S, and return the part before it, the separator itself, and the part after it. If the separator is not found, return S and two empty strings.
# 
# replace   
#     S.replace(old, new[, count]) -> string Return a copy of string S with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
# 
# rfind     
#     S.rfind(sub [,start [,end]]) -> int Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
# 
# rindex    
#     S.rindex(sub [,start [,end]]) -> int Like S.rfind() but raise ValueError when the substring is not found.
# 
# rjust     
#     S.rjust(width[, fillchar]) -> string Return S right-justified in a string of length width. Padding is done using the specified fill character (default is a space)
# 
# rpartition
#     S.rpartition(sep) -> (head, sep, tail) Search for the separator sep in S, starting at the end of S, and return the part before it, the separator itself, and the part after it. If the separator is not found, return two empty strings and S.
# 
# rsplit    
#     S.rsplit([sep [,maxsplit]]) -> list of strings Return a list of the words in the string S, using sep as the delimiter string, starting at the end of the string and working to the front. If maxsplit is given, at most maxsplit splits are done. If sep is not specified or is None, any whitespace string is a separator.
# 
# rstrip    
#     S.rstrip([chars]) -> string or unicode Return a copy of the string S with trailing whitespace removed. If chars is given and not None, remove characters in chars instead. If chars is unicode, S will be converted to unicode before stripping
# 
# split     
#     S.split([sep [,maxsplit]]) -> list of strings Return a list of the words in the string S, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done. If sep is not specified or is None, any whitespace string is a separator and empty strings are removed from the result.
# 
# splitlines
#     S.splitlines(keepends=False) -> list of strings Return a list of the lines in S, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
# 
# startswith
#     S.startswith(prefix[, start[, end]]) -> bool Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.
# 
# strip     
#     S.strip([chars]) -> string or unicode Return a copy of the string S with leading and trailing whitespace removed. If chars is given and not None, remove characters in chars instead. If chars is unicode, S will be converted to unicode before stripping
# 
# swapcase  
#     S.swapcase() -> string Return a copy of the string S with uppercase characters converted to lowercase and vice versa.
# 
# title     
#     S.title() -> string Return a titlecased version of S, i.e. words start with uppercase characters, all remaining cased characters have lowercase.
# 
# translate 
#     S.translate(table [,deletechars]) -> string Return a copy of the string S, where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256 or None. If the table argument is None, no translation is applied and the operation simply removes the characters in deletechars.
# 
# upper     
#     S.upper() -> string Return a copy of the string S converted to uppercase.
# 
# zfill     
#     S.zfill(width) -> string Pad a numeric string S with zeros on the left, to fill a field of the specified width. The string S is never truncated.
