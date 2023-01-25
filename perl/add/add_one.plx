#!/usr/bin/perl -w

use warnings;
use diagnostics;
use strict;

my %bo1;


sub main
{
    add_one();
}

sub add_one
{
    my $total = 0;
    my $sleep = 0;
    while ($total < 86400)
    {
        print "$sleep $total\n";
        $sleep++;
        $total += $sleep;
    }
}

main();
