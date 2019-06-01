#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    find_pngs();
}


sub makeDateTag
{
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $year -= 100;
    $mon++;
    # my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    my $tag = sprintf("%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min);
    # my $tag = sprintf("%02d%02d%02d", $year, $mon, $mday);
    return $tag;
}

sub find_pngs
{
    my $tag = makeDateTag();
    my $dir = "png$tag";
    mkdir $dir;
    my $glob = "../../Desktop/Screen*.png";
    my @glob = glob($glob);
    my $count = 0;
    foreach my $filename (@glob)
    {
        if ($filename =~ / Shot /)
        {
            $count++;
            my $fn = $filename;
            $fn =~ s/ /\\ /g;
            my $cmd1 = "mv $fn $dir/model$count.png";
            # print "mv $filename $dir/model$count.png\n";
            print "$cmd1\n";
            system($cmd1);
        }
    }
}

main();
