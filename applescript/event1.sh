# https://flylib.com/books/en/3.126.1.117/1/

# # http://mirror.informatimago.com/next/developer.apple.com/technotes/tn2004/tn2124.html
# 
# #https://developer.apple.com/library/archive/technotes/tn2124/_index.html#//apple_ref/doc/uid/DTS10003391-CH1-SECAE
# #Some environment variables—specifically AEDebug, AEDebugVerbose, AEDebugOSL, AEDebugFlattenedEvents, and AEDebugFile—are only supported by the debug library.
# #
# #If you are using the debug library, you can also control Apple event debugging by creating three files in /var/tmp:
# #
# #Creating the file /var/tmp/AEDebugFull is equivalent to setting the AEDebug, AEDebugSends, AEDebugReceives, AEDebugVerbose, AEDebugOSL, and AEDebugFlattenedEvents environment variables.
# #Creating the file /var/tmp/AEDebug.out is equivalent to setting AEDebugFile to "/var/tmp/AEDebug.out".
# #Creating the file /var/tmp/AEDebugLogs causes Apple Event Manager to send all of its output to a file named /var/tmp/AELog-<progname>.

export AEAEDebugFlattenedEvents=0
export AEDebugFull=1
export AEDebugOSL=1
export AEDebug=1
export AEDebugVerbose=1
export AEDebugSends=1
export AEDebugReceives=1
open /Applications/Safari.app
open http://www.apple.com

# # http://mirror.informatimago.com/next/developer.apple.com/technotes/tn2004/tn2124.html
# ApplicationServices
# 
# Apple Events
# 
# The Apple Event Manager has extensive built-in debugging support. The best way to learn about this support is use GDB to call the GDBPrintHelpDebuggingAppleEvents routine, as shown in Listing 30.
# 
# Listing 30: Apple Event Manager debugging help
# 
# (gdb) call (void) GDBPrintHelpDebuggingAppleEvents()
# The AppleEvent Manager has been completely rewritten for this
# version of Mac OS X.  The internal structure of an AEDesc is
# now a pointer to a sparse tree.  If you're having problems
# it could be because you're accessing the dataHandle of an
# AEDesc directly.
# 
# Also of note is that AEGetDescData and AEGetDescDataSize only
# work with value descriptors created by AECreateDesc - you cannot
# get the data size of an AERecord or AEList, for example.
# 
# To print the contents of an AppleEvent from GDB, you can:
#   (gdb) call (void) GDBPrintAEDesc(descPtr)
# 
# To view all currently installed AppleEvent coercion handlers:
#   (gdb) call (void) GDBPrintAECoercionTables()
# 
# To view all contents install AppleEvent handlers:
#   (gdb) call (void) GDBPrintAEHandlerTables()
# 
# Additionally, to log information about AppleEvent manager calls,
# you can set environment variables that will produce debugging output
# to the console:
# 
#   % setenv AEDebug         1            # general debug output
#   % setenv AEDebugSends    1            # print sent events
#   % setenv AEDebugReceives 1            # print received events and replies
#   % setenv AEDebugVerbose  1            # print result information on (most) \
#                                           calls (very verbose)
#   % setenv AEDebugOSL      1            # print result information from OSL
#   % setenv AEDebugFile     /tmp/logfile # send debug output to this file
# Note: In the above text, "this version of Mac OS X" refers to Mac OS X 10.2.
# 
# Some environment variables—specifically AEDebug, AEDebugVerbose, AEDebugOSL, and AEDebugFile—are only supported by the debug library.
# 
# If you are using the debug library, you can also control Apple event debugging by creating three files in /var/tmp.
# 
# Creating the file /var/tmp/AEDebug is equivalent to setting the AEDebug, AEDebugSends, AEDebugReceives, AEDebugReceives, and AEDebugOSL environment variables.
# 
# Creating the file /var/tmp/AEDebug.out is equivalent to setting AEDebugFile to "/var/tmp/AEDebug.out".
# 
# Creating the file /var/tmp/AEDebugLogs causes Apple Event Manager to send all of its output to a file named /var/tmp/AELog-<progname>.
# 
# IMPORTANT: The last two items only affect the destination of the debugging output. In order to produce debugging output, you have to enable it using one of the environment variables listed above, or by creating /var/tmp/AEDebug.
# 
# If you set the AE_PRINT_XML environment variable to 1 (10.4 and later), GDBPrintAEDesc will print the descriptor as XML (if possible).
# 
# 
