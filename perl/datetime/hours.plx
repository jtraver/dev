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
    hours()
}

sub hours
{
    my $hour = 1;
    my $hday = $hour * 24;
    my $hweek = $hday * 7;
    my $hmonth = $hday * 30;
    my $hyear = $hday * 365;
    print "$hour hour in one hour\n";
    print "$hday hours in one day\n";
    print "$hweek hours in one week\n";
    print "$hmonth hours in one month\n";
    print "$hyear hours in one year\n";
    my $hours = 1;
    for (my $i1 = 1; $i1 < 7; $i1++)
    {
        print "\n";
        print "$hours hours\n";
        my $h1 = $hours / $hour;
        my $d1 = $hours / $hday;
        my $w1 = $hours / $hweek;
        my $m1 = $hours / $hmonth;
        my $y1 = $hours / $hyear;
        print "  $h1 hours\n";
        print "  $d1 days\n";
        print "  $w1 weeks\n";
        print "  $m1 months\n";
        print "  $y1 years\n";
        $hours *= 10;
    }
    print "\n";
    print "10 hours is about half a day\n";
    print "100 hours is about half a week\n";
    print "1000 hours is about month\n";
    print "10000 hours is about year\n";
    print "100000 hours is about decade\n";
}

main();

#1709271230
#1 hour in one hour
#24 hours in one day
#168 hours in one week
#720 hours in one month
#8760 hours in one year
#
#1 hours
#  1 hours
#  0.0416666666666667 days
#  0.00595238095238095 weeks
#  0.00138888888888889 months
#  0.000114155251141553 years
#
#10 hours
#  10 hours
#  0.416666666666667 days
#  0.0595238095238095 weeks
#  0.0138888888888889 months
#  0.00114155251141553 years
#
#100 hours
#  100 hours
#  4.16666666666667 days
#  0.595238095238095 weeks
#  0.138888888888889 months
#  0.0114155251141553 years
#
#1000 hours
#  1000 hours
#  41.6666666666667 days
#  5.95238095238095 weeks
#  1.38888888888889 months
#  0.114155251141553 years
#
#10000 hours
#  10000 hours
#  416.666666666667 days
#  59.5238095238095 weeks
#  13.8888888888889 months
#  1.14155251141553 years
#
#100000 hours
#  100000 hours
#  4166.66666666667 days
#  595.238095238095 weeks
#  138.888888888889 months
#  11.4155251141553 years

