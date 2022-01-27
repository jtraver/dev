MMIX_HOME=~/mmix

MMIX_PROG=primes

$MMIX_HOME/mmixal-2 $MMIX_HOME/$MMIX_PROG.mms
# $MMIX_HOME/mmix-2 $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/$MMIX_PROG.mmconfig $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/$MMIX_PROG.mmconfig $MMIX_HOME/$MMIX_PROG.mmix
$MMIX_HOME/mmix-2 -D$MMIX_PROG.mmb $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_HOME/$MMIX_PROG.mmix
echo run about a million instructions
$MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_PROG.mmb
