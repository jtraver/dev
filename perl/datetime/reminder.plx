#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $do_popup = 1;
$do_popup = shift;

my @nremind;
$nremind[@nremind] = "neutrality";
$nremind[@nremind] = "amusement";
$nremind[@nremind] = "enthusiasm";
$nremind[@nremind] = "effort";
$nremind[@nremind] = "Be the Ghost";
$nremind[@nremind] = "Love is Choice";
$nremind[@nremind] = "If I'm not at choice I'm not in love";
$nremind[@nremind] = "all spiritual practice involves consciously redirecting attention";
$nremind[@nremind] = "once a spiritual practice becomes habitual, it is no longer a spiritual practice";

my @alarms;
my $alarms = 0;

my $SUN = 0;
my $MON = 1;
my $TUE = 2;
my $WED = 3;
my $THU = 4;
my $FRI = 5;
my $SAT = 6;

sub isRunning
{
    my @lines = `ps -ef`;
    my $count = 0;
    for my $line (@lines)
    {
        if ($line =~ /setAlarm.plx/)
        {
            print "$line\n";
            $count++;
        }
    }
    if ($count > 1)
    {
        exit(1);
    }
    $count = 0;
    @lines = `ps -alef`;
    for my $line (@lines)
    {
        if ($line =~ /setAlarm.plx/)
        {
            print "$line\n";
            $count++;
        }
    }
    if ($count > 1)
    {
        exit(1);
    }
}

sub setAlarms
{
    setAlarm($MON, 9, 15);
    setAlarm($MON, 20, 30);
    setAlarm($TUE, 11, 45);
    setAlarm($WED, 9, 15);
    # setAlarm($MON, 11, 19);
    # setAlarm($MON, 11, 22);
    # setAlarm($MON, 11, 25);
    # setAlarm($MON, 11, 28);
    # setAlarm($MON, 11, 31);
    # setAlarm($MON, 11, 34);
    # setAlarm($MON, 11, 37);
    # setAlarm($MON, 11, 40);
    # setAlarm($MON, 11, 43);
    # setAlarm($MON, 11, 46);
    # setAlarm($MON, 11, 49);
    # setAlarm($MON, 11, 52);
    # setAlarm($MON, 11, 55);
    # setAlarm($MON, 11, 58);
    # setAlarm($MON, 12, 1);
    # setAlarm($MON, 12, 4);
    # setAlarm($MON, 12, 7);
    # setAlarm($MON, 12, 10);
    # setAlarm($MON, 12, 13);
    # setAlarm($MON, 12, 16);
    # setAlarm($MON, 12, 19);
    # setAlarm($MON, 12, 22);
    # setAlarm($MON, 12, 25);
    # setAlarm($MON, 12, 28);
    # setAlarm($MON, 12, 31);
    # setAlarm($MON, 12, 34);
    # setAlarm($MON, 12, 37);
    # setAlarm($MON, 12, 40);
    # setAlarm($MON, 12, 43);
    # setAlarm($MON, 12, 46);
    # setAlarm($MON, 12, 49);
    # setAlarm($MON, 12, 52);
    # setAlarm($MON, 12, 55);
    # setAlarm($MON, 12, 58);
    # setAlarm($MON, 13, 1);
    # setAlarm($MON, 13, 4);
    # setAlarm($MON, 13, 7);
    # setAlarm($MON, 13, 10);
    # setAlarm($MON, 13, 13);
    # setAlarm($MON, 13, 16);
    # setAlarm($MON, 13, 19);
    # setAlarm($MON, 13, 22);
    # setAlarm($MON, 13, 25);
    # setAlarm($MON, 13, 28);
    # setAlarm($MON, 13, 31);
    # setAlarm($MON, 13, 34);
    # setAlarm($MON, 13, 37);
    # setAlarm($MON, 13, 40);
    # setAlarm($MON, 13, 43);
    # setAlarm($MON, 13, 46);
    # setAlarm($MON, 13, 49);
    # setAlarm($MON, 13, 52);
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

sub checkAlarms
{
    # print "\ncheckAlarms\n";
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
    my $smin = $min;
    my $shour = $hour;
    for (my $i1 = 0; $i1 < @alarms; $i1++)
    {
        $min = $smin;
        $hour = $shour;
        my $alarm = $alarms[$i1];
        # print "alarm = $alarm\n";
        my %hash = %$alarm;
        my $awday = $hash{'wday'};
        my $ahour = $hash{'hour'};
        my $amin = $hash{'min'};
        # print "checking alarm = $awday $ahour $amin\n";
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
        if ($ahour == $hour - 1)
        {
            if ($amin + 20 > 60)
            {
                $hour--;
                $min += 60;
            }
        }
        if ($ahour == $hour)
        {
            # print "we have an alarm this hour\n";
        }
        else
        {
            next;
        }
        # print "min = $min\n";
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
            print "first alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
        }
        if ($min == $amin + 5 && ($sec == 0 || $sec == 5 || $sec == 10 || $sec == 15 || $sec == 20 || $sec == 25 || $sec == 30))
        {
            print "second alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
            sleep(1);
            print "second alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
        }
        if ($min == $amin + 10 && ($sec == 0 || $sec == 5 || $sec == 10 || $sec == 15 || $sec == 20 || $sec == 25 || $sec == 30 || $sec == 35 || $sec == 40 || $sec == 45))
        {
            print "third  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
            sleep(1);
            print "third  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
            sleep(1);
            print "third  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
        }
        if ($min >= $amin + 15 && $sec % 5 == 0)
        {
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
            sleep(1);
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
            sleep(1);
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
            sleep(1);
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec\n";
        }
    }
}

sub old_main
{
    isRunning();
    setAlarms();
    while (1)
    {
        checkAlarms();
        sleep(1);
    }
}

sub main
{
    while (1)
    {
        my $index = int(rand(@nremind));
        my $reminder = $nremind[$index];
        print "$reminder is amusement\n";
        if ($do_popup == 1)
        {
            system("osascript window.osascript");
        }
        sleep(500);
    }
}

main();
