#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $program_name = $0;

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
    my $psline;
    for my $line (@lines)
    {
        if ($line =~ /setAlarm.plx/)
        {
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $line =~ s/^\s+//;
            $line =~ s/\s+$//;
            print "check1 $line\n";
            $psline = $line;
            $count++;
        }
    }
    if ($count >= 1)
    {
        print "psline $psline\n";
        my @fields = split(" ", $psline);
        for (my $i1 = 0; $i1 < @fields; $i1++)
        {
            my $v1 = $fields[$i1];
            print "$i1 $v1\n";
        }
        my $pid = $fields[1];
        print "pid = $pid\n";
        system("kill $pid");
        sleep(1);
        system("kill -1 $pid");
        sleep(1);
        system("kill -9 $pid");
        exit(1);
    }
    $count = 0;
    @lines = `ps -alef`;
    for my $line (@lines)
    {
        if ($line =~ /setAlarm.plx/)
        {
            print "check2 $line\n";
            $count++;
        }
    }
    if ($count > 1)
    {
        exit(1);
    }
}


# flush
$| = 1;

my $VT100_RED="[0;1;31m";
# really, "stop markup"; "bold"; "green"
my $VT100_GREEN="[0;1;32m";
my $VT100_YELLOW="[0;1;33m";
my $VT100_BLUE="[0;1;34m";
my $VT100_STOP_MARKUP="[0m";

sub myexit
{
    my ($fail) = @_;
    print STDERR "\n";
    if ($fail != 0)
    {
        print "FAIL $fail failures\n";
        print "DONE\n";
        exit($fail);
    }
    print "PASS\n";
    print "DONE\n";
    print "\n";
    exit($fail);
}

sub main
{
    print "program is $program_name\n";
    isRunning();
}

main();
