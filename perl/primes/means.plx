#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my @primes;
my %primes;
my %sums;
my $limit = 1000000;

sub is_prime
{
    my ($pc) = @_;

    # print "checking $pc\n";
    my $prime = 1;
    for (my $idiv = 1; $idiv < @primes; $idiv++)
    {
        my $div = $primes[$idiv];
        if ($div * $div > $pc)
        {
            last;
        }
        # print "div = $div\n";
        if ($pc % $div == 0)
        {
            $prime = 0;
        }
    }
    if ($prime && !defined($primes{$pc}))
    {
        $primes[@primes] = $pc;
        $primes{$pc} = $pc;
    }
    return $prime;
}

sub find_sums
{
    my ($dpc) = @_;
    
    my $pc = $dpc / 2;
    print "$pc";
    my $count = 0;
    for (my $i1 = 1; $i1 < @primes; $i1++)
    {
        my $s1 = $primes[$i1];
        for (my $i2 = $i1 + 1; $i2 < @primes; $i2++)
        {
            my $s2 = $primes[$i2];
            if ($s1 + $s2 == $dpc)
            {
                # print " ($s1 $s2)";
                $count++;
            }
        }
    }
    if ($count == 0)
    {
        print " zero\n";
    }
    elsif ($count == 1)
    {
        print " one\n";
    }
    else
    {
        print " $count\n";
    }
}

sub check_prime_mean
{
    my ($pc) = @_;

    my $dpc = $pc * 2;
    my $start = $primes[@primes - 1];
    if (!defined($start))
    {
        $start = 1;
    }
    for (my $i = $start; $i <= $dpc; $i++)
    {
        if (is_prime($i))
        {
            # print "$i is prime\n";
        }
        else
        {
            # print "$i is not prime\n";
        }
    }
    find_sums($dpc);
}

sub old_main
{
    my $pc = 1;
    while ($pc < 10000)
    {
        check_prime_mean($pc);
        $pc++;
    }
}

sub do_sums
{
    for (my $i1 = 2; $i1 < @primes - 1; $i1++)
    {
        my $s1 = $primes[$i1];
        for (my $i2 = $i1 + 1; $i2 < @primes; $i2++)
        {
            my $s2 = $primes[$i2];
            my $sum = $s1 + $s2;
            $sums{$sum}++;
        }
    }
    foreach my $num (sort {$a <=> $b} keys %sums)
    {
        my $count = $sums{$num};
        if ($num > $limit)
        {
            last;
        }
        if ($count == 0)
        {
            print "$num zero\n";
        }
        elsif ($count == 1)
        {
            print "$num one\n";
        }
        else
        {
            print "$num $count\n";
        }
    }
}

sub main
{
    my $pc = 1;
    while ($pc < $limit)
    {
        if (is_prime($pc))
        {
            # print "$pc is prime\n";
        }
        $pc++;
    }
    do_sums();
}

main();
