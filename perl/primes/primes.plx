my @primes;

$primes[0] = 2;
print "2";

my $mprime = 0;
my $max = 0;
my $pc = 3;
my $len = 0;
while ($pc < 10000000)
{
    # print "pc = $pc, len = $len, max = $max\n";
    $len++;
    $prime = 0;
    for (my $idiv = 0; $idiv < @primes; $idiv++)
    {
        my $div = $primes[$idiv];
        # print "pc = $pc, div = $div\n";
        my $lim = $div * $div;
        if ($lim > $pc)
        {
            $prime = $pc;
            $primes[@primes] = $prime;
            last;
        }
        if ($pc % $div == 0)
        {
            last;
        }
    }
    if ($prime)
    {
        print " ($len)";
        if ($len > $max)
        {
            $max = $len;
            print " max";
            $mprime = $prime;
        }
        $len = 0;
        print "\n";
        print "$prime";
    }
    else
    {
        print " $pc";
    }
    $pc++;
}
print "\n";
print "max $max at $mprime\n";
