MMIX_HOME=~/mmix

MMIX_PROG=primes

$MMIX_HOME/mmixal-2 -l $MMIX_PROG.lst $MMIX_HOME/$MMIX_PROG.mms
# vi $MMIX_PROG.lst
# $MMIX_HOME/mmix-2 -s $MMIX_HOME/$MMIX_PROG.mmo
$MMIX_HOME/mmix-2 -P $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmix-2 $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/$MMIX_PROG.mmconfig $MMIX_HOME/$MMIX_PROG.mmix
