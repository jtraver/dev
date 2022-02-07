MMIX_HOME=~/mmix

MMIX_PROG=hello3

# assembler
$MMIX_HOME/mmix-as $MMIX_PROG.mms -o $MMIX_PROG.o
# linker/loader
$MMIX_HOME/mmix-ld --oformat mmo $MMIX_PROG.o -o $MMIX_PROG.mmo
# simulator
$MMIX_HOME/mmix-2 $MMIX_PROG.mmo
