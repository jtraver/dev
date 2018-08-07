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

sub old_main
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
        # my $filler = sprintf("%*.s", $len3, "                                ");
        my $filler = sprintf("%.*s", $len3, "----------------------------------------------");
        print "$i1 $filler $str1\n";
        $str1 = "$str1$i1";
    }
}

sub main
{
    alphabet();
}

sub alphabet
{
    my @alpha;
    my $a0 = ord('a');
    print "a0 = $a0\n";
    for (my $i1 = 0; $i1 < 26; $i1++)
    {
        my $a1 = $a0 + $i1;
        my $s1 = sprintf("%c %d", $a1, $i1 + 1);
        print "$s1\n";
        $alpha[$a1] = $i1 + 1;
    }
    print "\n";
    my $od1 = ord('d');
    my $ad1 = $alpha[$od1];
    my $s1 = sprintf("%c %d", $od1, $ad1);
    print "$s1\n";

    my $or1 = ord('r');
    my $ar1 = $alpha[$or1];
    $s1 = sprintf("%c %d", $or1, $ar1);
    print "$s1\n";

    my $ou1 = ord('u');
    my $au1 = $alpha[$ou1];
    $s1 = sprintf("%c %d", $ou1, $au1);
    print "$s1\n";

    my $om1 = ord('m');
    my $am1 = $alpha[$om1];
    $s1 = sprintf("%c %d", $om1, $am1);
    print "$s1\n";

    my $op1 = ord('p');
    my $ap1 = $alpha[$op1];
    $s1 = sprintf("%c %d", $op1, $ap1);
    print "$s1\n";

    my $of1 = ord('f');
    my $af1 = $alpha[$of1];
    $s1 = sprintf("%c %d", $of1, $af1);
    print "$s1\n";

    print "\n";
    my $ot1 = ord('t');
    my $at1 = $alpha[$ot1];
    $s1 = sprintf("%c %d", $ot1, $at1);
    print "$s1\n";

    $or1 = ord('r');
    $ar1 = $alpha[$or1];
    $s1 = sprintf("%c %d", $or1, $ar1);
    print "$s1\n";

    $ou1 = ord('u');
    $au1 = $alpha[$ou1];
    $s1 = sprintf("%c %d", $ou1, $au1);
    print "$s1\n";

    $om1 = ord('m');
    $am1 = $alpha[$om1];
    $s1 = sprintf("%c %d", $om1, $am1);
    print "$s1\n";

    $op1 = ord('p');
    $ap1 = $alpha[$op1];
    $s1 = sprintf("%c %d", $op1, $ap1);
    print "$s1\n";

    # d 4
    # r 18
    # u 21
    # m 13
    # p 16
    # f 6
    my $df1 = $ad1 * $af1;
    print "d * f = $df1\n";
    my $mdf1 = $df1 + $am1;
    print "(d * f) + m = $mdf1\n";
    my $rmdf1 = $mdf1 * $ar1;
    print "r * ((d * f) + m) = $rmdf1\n";
    my $up1 = $au1 + $ap1;
    print "u + p = $up1\n";
    my $rup1 = $ar1 * $up1;
    print "r * (u + p) = $rup1\n";

    print "\n";
    # t 20
    # r 18
    # u 21
    # m 13
    # p 16
    print "u + p = $up1\n";
    print "r * (u + p) = $rup1\n";
    my $tm1 = $at1 * $am1;
    print "t * m = $tm1\n";
}

main();
