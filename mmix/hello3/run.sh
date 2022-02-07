MMIX_HOME=~/mmix

MMIX_PROG=hello3

# $MMIX_HOME/mmixal-2 --help
# $MMIX_HOME/mmixal-2 -h
$MMIX_HOME/mmixal-2 $MMIX_PROG.mms
# $MMIX_HOME/mmix-2 $MMIX_PROG.mmo
$MMIX_HOME/mmix-2 $MMIX_PROG
# $MMIX_HOME/mmix-2 -D$MMIX_PROG.mmb $MMIX_PROG.mmo
# echo entery at least 405 instruction steps to run the full program
# $MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_PROG.mmb

echo
# echo $MMIX_HOME/mmix-2 -t1 -l1000  $MMIX_PROG
# $MMIX_HOME/mmix-2 -t1 -l1000  $MMIX_PROG > $MMIX_PROG.trace
echo $MMIX_HOME/mmix-2 -b300 -v $MMIX_PROG
$MMIX_HOME/mmix-2 -b300 -v $MMIX_PROG > $MMIX_PROG.trace
vi $MMIX_PROG.trace

# $MMIX_HOME/mmix-2 -h
# $MMIX_HOME/mmix-2 -D$MMIX_PROG.dump $MMIX_PROG


#Usage: /home/jtraver/mmix/mmix-2 <options> progfile command line-args...
# with these options: (<n>=decimal number, <x>=hex number)
# -t<n> trace each instruction the first n times
# echo
# echo $MMIX_HOME/mmix-2 -t1 $MMIX_PROG
# $MMIX_HOME/mmix-2 -t1 $MMIX_PROG
# -e<x> trace each instruction with an exception matching x
# -r    trace hidden details of the register stack
# echo
# echo $MMIX_HOME/mmix-2 -r $MMIX_PROG
# $MMIX_HOME/mmix-2 -r $MMIX_PROG
# -l<n> list source lines when tracing, filling gaps <= n
# echo
# echo $MMIX_HOME/mmix-2 -t1 -l1000 $MMIX_PROG
# $MMIX_HOME/mmix-2 -t1 -l1000 $MMIX_PROG
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

