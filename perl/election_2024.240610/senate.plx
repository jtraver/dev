#!/usr/bin/perl -w

use IO::Handle;

use diagnostics;
use warnings;
use strict;

sub main
{
    senate("senate.240610");
}

sub senate
{
    my ($filename) = @_;
    print "senate: filename = $filename\n";
    my $file_open = open(SENATE, $filename);
    if (!$file_open)
    {
        print "ERROR senate: could not read filename = $filename";
        print "\n";
        return;
    }
    my @lines1 = <SENATE>;
    chomp(@lines1);
    for my $line1 (@lines1)
    {
        print "line1 = '$line1'\n";
    }
}

main();
