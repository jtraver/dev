#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my %files;

sub main
{
    print "stat link1\n";
    my @stat = stat("link1");
    foreach my $stat (@stat)
    {
        print "$stat\n";
    }

    print "lstat link1\n";
    my @lstat = lstat("link1");
    foreach my $lstat (@lstat)
    {
        print "$lstat\n";
    }

    print "stat stat1.plx\n";
    @stat = stat("stat1.plx");
    foreach my $stat (@stat)
    {
        print "$stat\n";
    }

    print "lstat stat1.plx\n";
    @lstat = lstat("stat1.plx");
    foreach my $lstat (@lstat)
    {
        print "$lstat\n";
    }

    show_links();
}

sub show_links
{
    print "\nshow links\n";
    my @glob = glob("*");
    foreach my $file (@glob)
    {
        print "$file\n";
        my $stat_ino = (stat($file))[1];
        $files{$stat_ino} = $file;
    }
    foreach my $file (@glob)
    {
        my $stat_ino = (stat($file))[1];
        my $sfile = $files{$stat_ino};
        print "$file -> $sfile\n";
    }
}

main();
