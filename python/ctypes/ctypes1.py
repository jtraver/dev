#!/usr/bin/python

import ctypes
# from ctypes import create_string_buffer
import apihelper

buf = ctypes.create_string_buffer(10)
print "buf = %s" % str(buf)
print "buf = %s" % str(type(buf))
print "buf = %s" % str(dir(buf))
buf[0] = 'a'
print "buf = %s" % str(buf.raw)
print "buf = %s" % str(buf[0])
print "buf = %x" % ord(buf[0])

apihelper.info(ctypes)

# c_bool     None
# c_buffer   None
# c_byte     None
# c_char     None
# c_char_p   None
# c_double   None
# c_float    None
# c_int      None
# c_int16    None
# c_int32    None
# c_int64    None
# c_int8     None
# c_long     None
# c_longdouble None
# c_longlong None
# c_short    None
# c_size_t   None
# c_ssize_t  None
# c_ubyte    None
# c_uint     None
# c_uint16   None
# c_uint32   None
# c_uint64   None
# c_uint8    None
# c_ulong    None
# c_ulonglong None
# c_ushort   None
# c_void_p   None
# c_voidp    None
# c_wchar    None
# c_wchar_p  None

print "bool = %s" % str(ctypes.sizeof(ctypes.c_bool))
try:
    print "buffer = %s" % str(ctypes.sizeof(ctypes.c_buffer))
except Exception as e:
    print "c_buffer e = %s" % str(e)
    print "c_buffer e = %s" % str(type(e))
print "byte = %s" % str(ctypes.sizeof(ctypes.c_byte))
print "char = %s" % str(ctypes.sizeof(ctypes.c_char))
print "char_p = %s" % str(ctypes.sizeof(ctypes.c_char_p))
print "double = %s" % str(ctypes.sizeof(ctypes.c_double))
print "float = %s" % str(ctypes.sizeof(ctypes.c_float))
print "int = %s" % str(ctypes.sizeof(ctypes.c_int))
print "int16 = %s" % str(ctypes.sizeof(ctypes.c_int16))
print "int32 = %s" % str(ctypes.sizeof(ctypes.c_int32))
print "int64 = %s" % str(ctypes.sizeof(ctypes.c_int64))
print "int8 = %s" % str(ctypes.sizeof(ctypes.c_int8))
print "long = %s" % str(ctypes.sizeof(ctypes.c_long))
print "longdouble = %s" % str(ctypes.sizeof(ctypes.c_longdouble))
print "longlong = %s" % str(ctypes.sizeof(ctypes.c_longlong))
print "short = %s" % str(ctypes.sizeof(ctypes.c_short))
print "size_t = %s" % str(ctypes.sizeof(ctypes.c_size_t))
print "ssize_t = %s" % str(ctypes.sizeof(ctypes.c_ssize_t))
print "ubyte = %s" % str(ctypes.sizeof(ctypes.c_ubyte))
print "uint = %s" % str(ctypes.sizeof(ctypes.c_uint))
print "uint16 = %s" % str(ctypes.sizeof(ctypes.c_uint16))
print "uint32 = %s" % str(ctypes.sizeof(ctypes.c_uint32))
print "uint64 = %s" % str(ctypes.sizeof(ctypes.c_uint64))
print "uint8 = %s" % str(ctypes.sizeof(ctypes.c_uint8))
print "ulong = %s" % str(ctypes.sizeof(ctypes.c_ulong))
print "ulonglong = %s" % str(ctypes.sizeof(ctypes.c_ulonglong))
print "ushort = %s" % str(ctypes.sizeof(ctypes.c_ushort))
print "void_p = %s" % str(ctypes.sizeof(ctypes.c_void_p))
print "voidp = %s" % str(ctypes.sizeof(ctypes.c_voidp))
print "wchar = %s" % str(ctypes.sizeof(ctypes.c_wchar))
print "wchar_p = %s" % str(ctypes.sizeof(ctypes.c_wchar_p))
