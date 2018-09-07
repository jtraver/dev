#https://developer.apple.com/library/archive/technotes/tn2124/_index.html#//apple_ref/doc/uid/DTS10003391-CH1-SECAE
#Some environment variables—specifically AEDebug, AEDebugVerbose, AEDebugOSL, AEDebugFlattenedEvents, and AEDebugFile—are only supported by the debug library.
#
#If you are using the debug library, you can also control Apple event debugging by creating three files in /var/tmp:
#
#Creating the file /var/tmp/AEDebugFull is equivalent to setting the AEDebug, AEDebugSends, AEDebugReceives, AEDebugVerbose, AEDebugOSL, and AEDebugFlattenedEvents environment variables.
#Creating the file /var/tmp/AEDebug.out is equivalent to setting AEDebugFile to "/var/tmp/AEDebug.out".
#Creating the file /var/tmp/AEDebugLogs causes Apple Event Manager to send all of its output to a file named /var/tmp/AELog-<progname>.

export AEDebug=1
export AEDebugVerbose=1
export AEDebugSends=1
export AEDebugReceives=1
# open /Applications/Safari.app
# open http://www.apple.com
# /usr/bin/osascript -e 'quit application "Finder"'
/usr/bin/open -a "Finder"
