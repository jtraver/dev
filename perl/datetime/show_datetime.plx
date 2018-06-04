#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $VT100_RED="[0;1;31m";
# really, "stop markup"; "bold"; "green"
my $VT100_GREEN="[0;1;32m";
my $VT100_YELLOW="[0;1;33m";
my $VT100_BLUE="[0;1;34m";
my $VT100_STOP_MARKUP="[0m";

my $reftime = shift;

sub setLocalTime
{
    my ($time) = @_;
    # print "time = $time\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($time);
    $year -= 100;
    $mon++;
    # sudo date 04161149.49
    my $tag = sprintf("%02d%02d%02d%02d.%02d", $mon, $mday, $hour, $min, $sec);
    system("sudo date $tag");
    return int($tag);
}


sub makeLocalDateTime
{
    my ($time) = @_;
    # print "time = $time\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($time);
    $year -= 100;
    $mon++;
    my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    return int($tag);
}


sub makeGMDateTime
{
    my ($time) = @_;
    # print "time = $time\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime($time);
    $year -= 100;
    $mon++;
    my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    return int($tag);
}



sub main
{
    my $time = time;
    print "$time\n";
    if (defined($reftime))
    {
        # my $diff = $time - $reftime;
        my $diff = $reftime - $time;
        if ($diff <= 1 && $diff >= -1)
        {
            print "ref time diff = $diff\n";
        }
        else
        {
            # print "ref time diff = $VT100_RED$diff$VT100_STOP_MARKUP\n";
            print "$VT100_RED ref time diff = $diff$VT100_STOP_MARKUP\n";
        }
        # setLocalTime($reftime);
    }
    else
    {
        # print "hello\n";
        # system("date");
        my $lt = makeLocalDateTime($time);
        # print "local time tag = $lt\n";
        my $gmt = makeGMDateTime($time);
        # print "gm time tag = $gmt\n";
        my $diff = $gmt - $lt;
        # print "diff time = $diff\n";
    }
}

main();

#SYNOPSIS
#    date [OPTION]... [+FORMAT]
#    date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]
# sudo date 04161149.49
