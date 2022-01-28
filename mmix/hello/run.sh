MMIX_HOME=~/mmix

MMIX_PROG=hello

$MMIX_HOME/mmixal-2 $MMIX_HOME/$MMIX_PROG.mms
$MMIX_HOME/mmix-2 $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/$MMIX_PROG.mmconfig $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/$MMIX_PROG.mmconfig $MMIX_HOME/$MMIX_PROG.mmix
$MMIX_HOME/mmix-2 -D$MMIX_PROG.mmb $MMIX_HOME/$MMIX_PROG.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_HOME/$MMIX_PROG.mmix
echo entery at least 405 instruction steps to run the full program
$MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_PROG.mmb
