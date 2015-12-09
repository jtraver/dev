#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my @primes;
my %primes;
my $limit = 10000;

$| = 1;

sub is_prime
{
    my ($pc) = @_;

    if ($pc < 1)
    {
        return 1;
    }
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

sub is_even
{
    my ($ec) = @_;

    return ($ec % 2) == 0;
}

sub next_prime
{
    my ($pc) = @_;

    for (my $i1 = 0; $i1 < @primes; $i1++)
    {
        my $prime = $primes[$i1];
        if ($prime > $pc)
        {
            return $prime;
        }
    }
}

sub main
{
    if (is_prime(0))
    {
        # print "0 is prime\n";
    }
    if (is_prime(1))
    {
        # print "1 is prime\n";
    }
    if (is_prime(2))
    {
        # print "2 is prime\n";
    }
    if (is_prime(3))
    {
        # print "3 is prime\n";
    }
    if (is_prime(4))
    {
        # print "4 is prime\n";
    }
    my $pc = 1;
    my $start = 1;
    my $max = 0;
    my $prime = 1;
    my $maxcount = 0;
    my $maxlower = 0;
    while ($pc < $limit)
    {
        if (is_prime($pc))
        {
            # print "$pc is prime\n";
        }
        else
        {
            # print "$pc is not prime\n";
        }
        if (is_even($pc))
        {
            $start = 1;
        }
        else
        {
            $start = 2;
        }
        if ($pc == 1)
        {
            $start = 1;
        }
        my $distance = $start;
        my $lower = $pc - $distance;
        my $upper = $pc + $distance;
        for (my $i1 = $pc; $i1 <= $upper; $i1++)
        {
            if (!is_even($i1))
            {
                is_prime($i1);
            }
        }
        while (!(is_prime($lower) && is_prime($upper)))
        {
            $distance += 2;
            $lower = $pc - $distance;
            $upper = $pc + $distance;
            for (my $i1 = $pc; $i1 <= $upper; $i1++)
            {
                if (!is_even($i1))
                {
                    is_prime($i1);
                }
            }
        }
        if (is_prime($pc))
        {
            print "$pc\n";
            my $count1 = 0;
            my $lastlower = 0;
            for (my $i3 = 1; $i3 <= $pc; $i3++)
            {
                my $tlower = $pc - $i3;
                my $tupper = $pc + $i3;
                if (is_prime($tlower) && is_prime($tupper))
                {
                    print "  $tlower + $tupper\n";
                    $count1++;
                    $lastlower = $tlower;
                }
            }
            if ($lastlower > $maxlower)
            {
                $maxlower = $lastlower;
                print "    $maxlower new lower maximum for $pc\n";
            }
            if ($count1 > $maxcount)
            {
                $maxcount = $count1;
                print "    $count1 pairs new max for $pc\n";
            }
            else
            {
                print "    $count1 pairs for $pc\n";
            }
            if ($count1 == 0)
            {
                print "  FAIL!\n";
                last;
            }
        }
        $pc++;
    }
    for (my $i1 = 0; $i1 < @primes; $i1++)
    {
        my $prime = $primes[$i1];
        # print "$i1 $prime\n";
    }
}

main();
