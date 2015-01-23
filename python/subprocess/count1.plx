#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $limit1 = 1000;
# my $limit1 = 10;

sub makeDateTag
{
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $year -= 100;
    $mon++;
    my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    # my $tag = sprintf("%02d%02d%02d", $year, $mon, $mday);
    return $tag;
}

sub main
{
    my $tag = makeDateTag();
    my $output = "count1.$tag";
    open(OUTPUT, ">$output") or die "Can't write $output: $!";
    for (my $i1 = 0; $i1 < $limit1; $i1++)
    {
        my $time = time;
        print "$i1 $time\n";
        print OUTPUT "$i1 $time\n";
        sleep(1);
    }
    close(OUTPUT);
}

main();
