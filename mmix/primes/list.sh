MMIX_HOME=~/mmix

$MMIX_HOME/mmixal-2 -l primes.lst $MMIX_HOME/primes.mms
vi primes.lst
$MMIX_HOME/mmix-2 $MMIX_HOME/primes.mmo
# $MMIX_HOME/mmmix-2 $MMIX_HOME/primes.mmconfig $MMIX_HOME/primes.mmo
$MMIX_HOME/mmmix-2 $MMIX_HOME/primes.mmconfig $MMIX_HOME/primes.mmix
