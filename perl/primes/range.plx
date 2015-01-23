#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my @primes;
my %primes;
my $limit = 10000;

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
        while (!(is_prime($lower) && is_prime($upper)))
        {
            $distance += 2;
            $lower = $pc - $distance;
            $upper = $pc + $distance;
        }
        if ($distance > $max)
        {
            $max = $distance;
            print "$pc has distance $distance at $lower and $upper\n";
        }
        $pc++;
    }
}

main();
