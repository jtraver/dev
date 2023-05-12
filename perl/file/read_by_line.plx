#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my %files;
my %inodes;
my %links;

sub main
{
    read_by_line();
}

sub read_by_line
{
    my $filename = "read_by_line.plx";
    my $fileopen = open(FH, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    while(<FH>)
    {
        print $_;
    }
}

main();
