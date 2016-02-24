#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use Getopt::Long;

sub show_inc
{
    foreach my $dir (@INC)
    {
        print "$dir\n";
        system("find $dir -name '*.pm'");
    }
}

sub main
{
    show_inc();
}

main();
