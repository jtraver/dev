#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my @alarms;
my $alarms = 0;

my $SUN = 0;
my $MON = 1;
my $TUE = 2;
my $WED = 3;
my $THU = 4;
my $FRI = 5;
my $SAT = 6;

sub setAlarms
{
    setAlarm($MON, 12, 19);
    setAlarm($MON, 12, 22);
    setAlarm($MON, 12, 25);
    setAlarm($MON, 12, 28);
    setAlarm($MON, 12, 31);
    setAlarm($MON, 12, 34);
    setAlarm($MON, 12, 37);
    setAlarm($MON, 12, 40);
    setAlarm($MON, 12, 43);
    setAlarm($MON, 12, 46);
}

sub setAlarm
{
    my ($wday, $hour, $min) = @_;
    my %alarm;
    $alarm{'wday'} = $wday;
    $alarm{'hour'} = $hour;
    $alarm{'min'} = $min;
    $alarms[$alarms++] = \%alarm;
}

# Execute anytime before the <STDIN>.
# Causes the currently selected handle to be flushed after every print.
# flush
$| = 1;

my $VT100_RED="[0;1;31m";
# really, "stop markup"; "bold"; "green"
my $VT100_GREEN="[0;1;32m";
my $VT100_YELLOW="[0;1;33m";
my $VT100_BLUE="[0;1;34m";
my $VT100_STOP_MARKUP="[0m";

sub main
{
    setAlarms();
    while (1)
    {
        checkAlarm();
        sleep(1);
    }
}

sub checkAlarm
{
    my $time = time;
    # print "time = $time\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($time);
    $year -= 100;
    $mon++;
    my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    # print "$tag wday = $wday $hour $min\n";
    if ($sec % 5 != 0)
    {
        return;
    }
    for (my $i1 = 0; $i1 < @alarms; $i1++)
    {
        my $alarm = $alarms[$i1];
        # print "alarm = $alarm\n";
        my %hash = %$alarm;
        my $awday = $hash{'wday'};
        my $ahour = $hash{'hour'};
        my $amin = $hash{'min'};
        print "checking alarm = $awday $ahour $amin\n";
        # print "awday = $awday\n";
        if ($awday == $wday)
        {
            # print "we have an alarm today\n";
        }
        else
        {
            next;
        }
        # print "ahour = $ahour\n";
        if ($ahour == $hour)
        {
            # print "we have an alarm this hour\n";
        }
        else
        {
            next;
        }
        # print "amin = $amin\n";
        if ($min >= $amin && $min <= $amin + 20)
        {
            # print "we are in an alarm period\n";
        }
        else
        {
            next;
        }
        if ($min == $amin && ($sec == 0 || $sec == 5 || $sec == 10 || $sec == 15))
        {
            print "alarm $awday $ahour $amin at $tag wday = $wday $hour $min $sec\n";
        }
        if ($min == $amin + 5 && ($sec == 0 || $sec == 5 || $sec == 10 || $sec == 15 || $sec == 20 || $sec == 25 || $sec == 30))
        {
            print "alarm $awday $ahour $amin at $tag wday = $wday $hour $min $sec\n";
        }
        if ($min == $amin + 10 && ($sec == 0 || $sec == 5 || $sec == 10 || $sec == 15 || $sec == 20 || $sec == 25 || $sec == 30 || $sec == 35 || $sec == 40 || $sec == 45))
        {
            print "alarm $awday $ahour $amin at $tag wday = $wday $hour $min $sec\n";
        }
        if ($min >= $amin + 15 && $sec % 5 == 0)
        {
            print "alarm $awday $ahour $amin at $tag wday = $wday $hour $min $sec\n";
        }
    }
}

main();
