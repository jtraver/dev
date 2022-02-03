MMIX_HOME=~/mmix

MMIX_PROG=hello2

# $MMIX_HOME/mmixal-2 --help
# $MMIX_HOME/mmixal-2 -h
$MMIX_HOME/mmixal-2 $MMIX_PROG.mms
# $MMIX_HOME/mmix-2 $MMIX_PROG.mmo
$MMIX_HOME/mmix-2 $MMIX_PROG
# $MMIX_HOME/mmix-2 -D$MMIX_PROG.mmb $MMIX_PROG.mmo
# echo entery at least 405 instruction steps to run the full program
# $MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_PROG.mmb

echo
echo running simulator with -P
$MMIX_HOME/mmix-2 -P $MMIX_PROG
$MMIX_HOME/mmix-2 -h
# $MMIX_HOME/mmix-2 -D$MMIX_PROG.dump $MMIX_PROG


#Usage: /home/jtraver/mmix/mmix-2 <options> progfile command line-args...
# with these options: (<n>=decimal number, <x>=hex number)
# -t<n> trace each instruction the first n times
# -e<x> trace each instruction with an exception matching x
# -r    trace hidden details of the register stack
# -l<n> list source lines when tracing, filling gaps <= n
# -s    show statistics after each traced instruction
# -P    print a profile when simulation ends
# -L<n> list source lines with the profile
# -v    be verbose: show almost everything
# -q    be quiet: show only the simulated standard output
# -i    run interactively (prompt for online commands)
# -I    interact, but only after the program halts
# -b<n> change the buffer size for source lines
# -c<n> change the cyclic local register ring size
# -f<filename> use given file to simulate standard input
# -D<filename> dump a file for use by other simulators

