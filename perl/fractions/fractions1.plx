#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    for (my $i1 = 1; $i1 <= 100; $i1++)
    {
        print "\n$i1\n";
        fractions($i1);
    }
}

sub fractions
{
    my ($t1) = @_;

    my %fractions;
    for (my $d1 = 1; $d1 <= $t1; $d1++)
    {
        for (my $n1 = 0; $n1 < $d1; $n1++)
        {
            my $fraction = $n1 / $d1;
            # print "$n1 / $d1 = $fraction\n";
            $fractions{$fraction}{$n1}{$d1} = 1;
        }
    }
    foreach my $fraction (sort { $a <=> $b } keys %fractions)
    {
        print "$fraction\n";
        my $nref = $fractions{$fraction};
        my %nhash = %$nref;
        foreach my $n1 (sort { $a <=> $b } keys %nhash)
        {
            # print "  $n1\n";
            my $dref = $nhash{$n1};
            my %dhash = %$dref;
            foreach my $d1 (sort { $a <=> $b } keys %dhash)
            {
                print "    $n1 / $d1\n";
            }
        }
    }
}

main();
