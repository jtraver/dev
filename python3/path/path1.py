#!/usr/bin/env python3
#!/usr/bin/python

import apihelper
import os

apihelper.info(os.path)

pathname = "/data/downloads/release/tools/3.11.0/aerospike-tools-3.11.0-debian8.tgz"
print "pathname = %s" % str(pathname)
basename = os.path.basename(pathname)
print "basename = %s" % str(basename)
root, ext = os.path.splitext(basename)
print "root = %s" % str(root)
print "ext = %s" % str(ext)
tgzdir = os.path.join(os.getcwd(), root)
print "tgzdir = %s" % str(tgzdir)


# 
# 
# _joinrealpath
#     None
# 
# _unicode  
#     unicode(object='') -> unicode object unicode(string[, encoding[, errors]]) -> unicode object Create a new Unicode object from the given encoded string. encoding defaults to the current default string encoding. errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.
# 
# abspath   
#     Return an absolute path.
# 
# basename  
#     Returns the final component of a pathname
# 
# commonprefix
#     Given a list of pathnames, returns the longest common leading component
# 
# dirname   
#     Returns the directory component of a pathname
# 
# exists    
#     Test whether a path exists. Returns False for broken symbolic links
# 
# expanduser
#     Expand ~ and ~user constructions. If user or $HOME is unknown, do nothing.
# 
# expandvars
#     Expand shell variables of form $var and ${var}. Unknown variables are left unchanged.
# 
# getatime  
#     Return the last access time of a file, reported by os.stat().
# 
# getctime  
#     Return the metadata change time of a file, reported by os.stat().
# 
# getmtime  
#     Return the last modification time of a file, reported by os.stat().
# 
# getsize   
#     Return the size of a file, reported by os.stat().
# 
# isabs     
#     Test whether a path is absolute
# 
# isdir     
#     Return true if the pathname refers to an existing directory.
# 
# isfile    
#     Test whether a path is a regular file
# 
# islink    
#     Test whether a path is a symbolic link
# 
# ismount   
#     Test whether a path is a mount point
# 
# join      
#     Join two or more pathname components, inserting '/' as needed. If any component is an absolute path, all previous path components will be discarded. An empty last part will result in a path that ends with a separator.
# 
# lexists   
#     Test whether a path exists. Returns True for broken symbolic links
# 
# normcase  
#     Normalize case of pathname. Has no effect under Posix
# 
# normpath  
#     Normalize path, eliminating double slashes, etc.
# 
# realpath  
#     Return the canonical path of the specified filename, eliminating any symbolic links encountered in the path.
# 
# relpath   
#     Return a relative version of a path
# 
# samefile  
#     Test whether two pathnames reference the same actual file
# 
# sameopenfile
#     Test whether two open file objects reference the same file
# 
# samestat  
#     Test whether two stat buffers reference the same file
# 
# split     
#     Split a pathname. Returns tuple "(head, tail)" where "tail" is everything after the final slash. Either part may be empty.
# 
# splitdrive
#     Split a pathname into drive and path. On Posix, drive is always empty.
# 
# splitext  
#     Split the extension from a pathname. Extension is everything from the last dot to the end, ignoring leading dots. Returns "(root, ext)"; ext may be empty.
# 
# walk      
#     Directory tree walk with callback function. For each directory in the directory tree rooted at top (including top itself, but excluding '.' and '..'), call func(arg, dirname, fnames). dirname is the name of the directory, and fnames a list of the names of the files and subdirectories in dirname (excluding '.' and '..'). func may modify the fnames list in-place (e.g. via del or slice assignment), and walk will only recurse into the subdirectories whose names remain in fnames; this can be used to implement a filter, or to impose a specific order of visiting. No semantics are defined for, or required of, arg, beyond that arg is always passed to func. It can be used, e.g., to pass a filename pattern, or a mutable object designed to accumulate statistics. Passing None for arg is common.
