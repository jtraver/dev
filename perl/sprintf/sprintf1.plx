#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

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

sub main
{
    my $tag = makeDateTag();
    print "$tag\n";
    adjustwidth();
}

sub adjustwidth
{
    my $width = 20;
    my $str1 = "a";
    for (my $i1 = 0; $i1 < $width; $i1++)
    {
        my $len1 = length($str1);
        my $si1 = "$i1";
        my $len2 = length($si1);
        my $len3 = $width - ($len1 + $len2);
        # print "len3 = $len3\n";
        if ($len3 <= 0)
        {
            last;
        }
        my $filler = sprintf("%*.s", $len3, "                                ");
        print "$i1 $filler $str1\n";
        $str1 = "$str1$i1";
    }
}

main();
