#!/usr/bin/perl -w

use IO::Handle;

use diagnostics;
use warnings;
use strict;

my %files;
my %inodes;
my %links;

# https://stackoverflow.com/questions/33812618/can-you-force-flush-output-in-perl

sub main
{
    read_by_line();
}

sub read_by_line
{
    my $filename = "flush1.plx";
    my $fileopen = open(FH, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    while(<FH>)
    {
        print STDERR $_;
        print $_;
        STDOUT->flush();
    }
    STDERR->flush();
}

main();
