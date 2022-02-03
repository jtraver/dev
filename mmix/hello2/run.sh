MMIX_HOME=~/mmix

MMIX_PROG=hello2

$MMIX_HOME/mmixal-2 $MMIX_PROG.mms
$MMIX_HOME/mmix-2 $MMIX_PROG.mmo
$MMIX_HOME/mmix-2 -D$MMIX_PROG.mmb $MMIX_PROG.mmo
echo entery at least 405 instruction steps to run the full program
$MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_PROG.mmb
