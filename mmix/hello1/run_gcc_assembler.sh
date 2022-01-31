MMIX_HOME=~/mmix

MMIX_PROG=hello1

# http://mmix.cs.hm.edu/examples/hellognu.html

# $MMIX_HOME/mmixal-2 $MMIX_PROG.mms
# $MMIX_HOME/mmix-2 $MMIX_PROG.mmo
# $MMIX_HOME/mmix-2 -D$MMIX_PROG.mmb $MMIX_PROG.mmo
# echo entery at least 405 instruction steps to run the full program
# $MMIX_HOME/mmmix-2 $MMIX_HOME/plain.mmconfig $MMIX_PROG.mmb

# assembler
$MMIX_HOME/mmix-as $MMIX_PROG.mms -o $MMIX_PROG.o
# linker/loader
$MMIX_HOME/mmix-ld --oformat mmo $MMIX_PROG.o -o $MMIX_PROG.mmo
# mmix-ld.exe --oformat mmo hello.o -o hello.mmo
$MMIX_HOME/mmix-2 $MMIX_PROG.mmo



#[jtraver@E1 hello1]$ run_gcc_assembler.sh 
#Can't open the object file hello1.mmo or hello1.mmo.mmo!
#[jtraver@E1 hello1]$ ls
#clean.sh  hello1.mms  hello1.mmo  hello1.o  run_gcc_assembler.sh  run.sh
#[jtraver@E1 hello1]$ 

