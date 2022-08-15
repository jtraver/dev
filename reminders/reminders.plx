#!/usr/bin/env perl -w

#!/usr/bin/perl -w

use diagnostics;
use strict;
use warnings;
use IO::Select;

my $program_name = $0;
my $reminder_time = shift;
if (!defined($reminder_time))
{
    $reminder_time = 60 * 15;
}

my @alarms;
my $alarms = 0;

my $SUN = 0;
my $MON = 1;
my $TUE = 2;
my $WED = 3;
my $THU = 4;
my $FRI = 5;
my $SAT = 6;

sub reminders
{
    # https://stackoverflow.com/questions/33973515/waiting-for-a-defined-period-of-time-for-the-input-in-perl
    my $select = IO::Select->new();
    $select->add( \*STDIN );
    print "start reminders\n";
    print "now sleeping $reminder_time\n";
    sleep($reminder_time);

    print "this is a reminder\n";
    print "\n";
    print "\n";
    my $input = "NONE";
    if ( $select->can_read(10) ) {
        $input = <STDIN>;
    }
    print "Got input of $input\n";
}

sub main
{
    print "program is $program_name\n";
    isRunning();
    # setAlarms();
    reminders();
    #while (1)
    #{
    #    checkAlarms();
    #    sleep(1);
    #}
}

sub setAlarms
{
    # setAlarm($FRI, 7, 52, "covid test 8");
    # setAlarm($FRI, 7, 35, "covid test 8");
    # setAlarm($THU, 7, 14, "meeting");
    # setAlarm($THU, 8, 0, "covid test 7");
    # setAlarm($WED, 8, 0, "covid test 6");
    # setAlarm($TUE, 8, 4, "covid test 5");
    # setAlarm($MON, 11, 55, "covid test 4");
    # setAlarm($SUN, 18, 0, "covid test 3");
    # setAlarm($FRI, 17, 2, "covid test 2");
    # setAlarm($THU, 16, 44, "brown bag meet.google.com/qhk-hbfj-ijt");
    # setAlarm($THU, 13, 14, "brown bag meet.google.com/eiv-uznw-cjx");
    # setAlarm($WED, 11, 44, "brown bag meet.google.com/ruy-huhc-ziz");
    # setAlarm($MON, 23, 4, "covid test 2");
    # setAlarm($MON, 22, 50, "covid test 1");
    # setAlarm($SUN, 7, 59, "plane to CA");
    # setAlarm($SUN, 7, 45, "plane to CA");
    # setAlarm($SUN, 7, 30, "plane to CA");
    # setAlarm($SUN, 7, 15, "plane to CA");
    # setAlarm($SUN, 7, 0, "plane to CA");
    # setAlarm($FRI, 12, 59, "hot spot");
    # setAlarm($WED, 12, 14, "Dentist 1:30pm 220720 wednesday July 20");
    # setAlarm($WED, 12, 44, "Dentist 1:30pm 220720 wednesday July 20");
    # setAlarm($FRI, 10, 44, "Alexandra Paretta +1 (949) 547-4959");
    # setAlarm($TUE, 15, 44, "talk to Danny about Gabe's number");
    # Tuesday meeting after a US holiday
    # setAlarm($TUE, 8, 44, "July 4th Holiday Tuesday meeting full QE winter time https://meet.google.com/gvv-rsdx-mtv");
    # setAlarm($FRI, 13, 44, "meet Nate meet.google.com/hwo-jpdp-bcj");
    # setAlarm($TUE, 12, 59, "qe offsite lunch");
    # setAlarm($WED, 8, 44, "company meeting");
    # setAlarm($TUE, 13, 29, "Nathaniel Larsen panel sync 	meet.google.com/zae-jfdn-dng");
    # setAlarm($FRI, 14, 14, "Kenny Collings meet.google.com/swu-zxza-bvm");
    # setAlarm($THU, 13, 29, "interview 2-3 Nathaniel Larsen meet.google.com/pwk-wifv-mhs");
    # setAlarm($THU, 13, 44, "interview 2-3 Nathaniel Larsen meet.google.com/pwk-wifv-mhs");
    # setAlarm($WED, 11, 29, "interview 12-1Nathaniel Larsen  meet.google.com/sar-mgbx-upw");
    # setAlarm($WED, 11, 44, "interview 12-1Nathaniel Larsen  meet.google.com/sar-mgbx-upw");
    # setAlarm($MON, 13, 29, "interview Kenny Collings meet.google.com/gki-ueju-eez");
    # setAlarm($MON, 13, 44, "interview meet.google.com/gki-ueju-eez");
    # setAlarm($TUE, 14, 29, "interview meet.google.com/oes-wfoe-jdw");
    # setAlarm($TUE, 14, 44, "interview meet.google.com/oes-wfoe-jdw");
    # setAlarm($TUE, 8, 44, "company meeting");
    # setAlarm($TUE, 13, 14, "dentist");
    # setAlarm($WED, 10, 14, "dentist 11 am");
    # setAlarm($TUE, 10, 14, "roof");
    # setAlarm($WED, 8, 44, "company meeting");
    # setAlarm($WED, 9, 44, "dentist");
    # setAlarm($SUN, 3, 44, "flight");
    # setAlarm($TUE, 14, 14, "ARM testing 	meet.google.com/rzo-xcvx-diw");
    # setAlarm($TUE, 8, 44, "company meeting https://aerospike.zoom.us/j/82613667955?pwd=aXFXZDQzQys3MFY5Y1JvcW9XcUNVQT09#success");
    # setAlarm($THU, 16, 29, "restorative health 	meet.google.com/exu-hvxv-biu");
    # setAlarm($TUE, 14, 44, "Review Dell Server Quote 	meet.google.com/cnc-sjdy-pqd");
    # setAlarm($WED, 8, 44, "Wed Feb 2, 2022 9am – 10:15am (MST) Where	Zoom Meeting - to be added Who	Aerospike, michael\@aerospike.com*");
    # setAlarm($WED, 8, 44, "Company Meeting zoom");
    # setAlarm($THU, 14, 14, "partition/paginated scan with disruption 	meet.google.com/jhh-isvi-tco");
    # setAlarm($TUE, 12, 0, "12:30 dentist appointment Tue 25 Jan 22");
    # setAlarm($WED, 8, 44, "Wed Feb 2, 2022 9am – 10:15am (MST) Where	Zoom Meeting - to be added Who	Aerospike, michael\@aerospike.com*");
    # setAlarm($WED, 8, 44, "Wed Feb 2, 2022 9am – 10:15am (MST) Where	Zoom Meeting - to be added Who	Aerospike, michael\@aerospike.com*");
    # setAlarm($WED, 14, 44, "andrew hello meet.google.com/uof-ajuu-crg");
    # setAlarm($TUE, 15, 44, "Diane 	meet.google.com/ncw-nnwk-opz");
    # setAlarm($SUN, 10, 52, "flip shrimp");
    # setAlarm($TUE, 19, 14, "reading +1-530-812-0772");
    # setAlarm($THU, 6, 0, "detroit");
    # setAlarm($TUE, 12, 44, "keta refill meet.google.com/zzd-rrqt-tvo");
    # setAlarm($FRI, 13, 44, "mark and howard 	meet.google.com/mnz-ygwb-ngw ");
    # setAlarm($FRI, 10, 9, "dentist");
    # setAlarm($WED, 14, 44, "dentist");
    # setAlarm($WED, 8, 44, "company meeting");
    # setAlarm($WED, 13, 44, "satellite");
    # setAlarm($TUE, 10, 44, "VMs 	meet.google.com/fgy-mkyx-cig ");
    # setAlarm($TUE, 9, 14, "QE meeting change");
    # setAlarm($TUE, 9, 44, "Dentist");
    # setAlarm($TUE, 10, 44, "Mark Karen John");
    # setAlarm($TUE, 13, 0, "Keta");
    # setAlarm($MON, 13, 29, "HealthSpot");
    # setAlarm($THU, 14, 14, "mark-john 	meet.google.com/xxo-wzeu-ssq");
    # setAlarm($WED, 14, 14, "scan options");
    # setAlarm($WED, 19, 14);
    # setAlarm($THU, 10, 44, "lunch with Roger");
    # setAlarm($THU, 14, 44, "remote docker meeting");
    # setAlarm($TUE, 9, 14, "tmp meeting due to holidays");
    # setAlarm($WED, 13, 0, "doctor");
    # setAlarm($MON, 13, 45, "doctor");
    # setAlarm($MON, 10, 30, "fasting");
    # setAlarm($WED, 14, 30, "tea");
    # setAlarm($TUE, 10, 44, "Mark");
    # setAlarm($TUE, 7, 44, "Dentist");
    # setAlarm($FRI,21, 0, "shrimp");
    # setAlarm($THU, 8, 44, "company meeting");
    # setAlarm($SAT,10, 44, "leave hyatt");
    # setAlarm($FRI,8, 44, "company meeting");
    # setAlarm($WED,8, 44, "resiliency meeting");
    # setAlarm($TUE,10, 44, "Mark meeting");
    # setAlarm($WED, 8, 44, "company meeting");
    # setAlarm($WED, 13, 24, "check jury selection webex meeting at 1:40");
    # setAlarm($WED, 10, 29, "leave hyatt for doctor");
    # setAlarm($WED, 10, 0, "get ready for doctor");
    # setAlarm($TUE, 9, 14, "memorial holiday QE meeting");
    # setAlarm($WED, 8, 44, "company meeting");
    # setAlarm($TUE, 12, 0, "doctor");
    # setAlarm($THU, 13, 0, "doctor");
    # setAlarm($WED, 11, 0, "dentist");
    # setAlarm($TUE, 9, 44, "summit tuesday");
    # setAlarm($WED, 9, 44, "summit wednesday");
    # setAlarm($THU, 9, 44, "summit thursday");
    # run all exp tests
    my $run_all_exp_tests = 0;
    if ($run_all_exp_tests == 1)
    {
        setAlarm($MON, 8, 0, "check exp test reminder");
        setAlarm($TUE, 8, 0, "check exp test reminder");
        setAlarm($WED, 8, 0, "check exp test reminder");
        setAlarm($THU, 8, 0, "check exp test reminder");
        setAlarm($FRI, 8, 0, "check exp test reminder");
        setAlarm($SAT, 8, 0, "check exp test reminder");
        setAlarm($SUN, 8, 0, "check exp test reminder");
        setAlarm($MON, 20, 0, "run exp test reminder");
        setAlarm($TUE, 20, 0, "run exp test reminder");
        setAlarm($WED, 20, 0, "run exp test reminder");
        setAlarm($THU, 20, 0, "run exp test reminder");
        setAlarm($FRI, 20, 0, "run exp test reminder");
        setAlarm($SAT, 20, 0, "run exp test reminder");
        setAlarm($SUN, 20, 0, "run exp test reminder");
    }

    # meetings
    # MONDAY QE
    setAlarm($MON, 8, 44, "monday full QE winter time https://meet.google.com/gvv-rsdx-mtv");
    # setAlarm($MON, 9, 14, "monday full QE");
    # MONDAY DEV
    setAlarm($MON, 11, 44, "monday dev https://meet.google.com/dmg-jxqp-bfc");
    # TUESDAY DEV
    # setAlarm($TUE, 11, 44);
    # WEDNESDAY/THURDAY QE CORE
    # setAlarm($THU, 8, 44, "new resiliency 	meet.google.com/cfk-wqsm-byv");
    setAlarm($THU, 8, 14, "new resiliency 	meet.google.com/cfk-wqsm-byv");
    # setAlarm($THU, 9, 14, "thursday core QE https://meet.google.com/cfk-wqsm-byv");
    # setAlarm($WED, 19, 14);

    # GARBAGE
    # garbage
    setAlarm($TUE, 8, 0, "garbage tuesday morning (summer)");
    setAlarm($MON, 13, 0, "garbage monday afternoon (winter)");
    # setAlarm($MON, 16, 0);
    # setAlarm($MON, 20, 0, "garbage monday evening (summer)");
    # setAlarm($MON, 19, 0);
    # setAlarm($MON, 20, 0);
    # setAlarm($MON, 18, 0);
    # setAlarm($MON, 16, 0);

    # walk
    my $walk = 0;
    if ($walk == 1)
    {
        setAlarm($MON, 13, 0);
        setAlarm($TUE, 13, 0);
        setAlarm($WED, 13, 0);
        setAlarm($THU, 13, 0);
        setAlarm($FRI, 13, 0);
        setAlarm($SAT, 13, 0);
        setAlarm($SUN, 13, 0);
    }

    # company meeting
    # setAlarm($TUE, 8, 14);
    # setAlarm($TUE, 8, 29);
    # setAlarm($TUE, 8, 44);
    # dentist
    # setAlarm($WED, 10, 04);
    # setAlarm($WED, 10, 44);
    # setAlarm($WED, 10, 59);
    # company meeting
    # setAlarm($WED, 8, 44);
    # setAlarm($TUE, 9, 14);
    # company meeting
    # setAlarm($TUE, 8, 44);
    # dentist Wed 24 Jun 20
    # setAlarm($WED, 12, 14);
    # setAlarm($WED, 11, 59);
    # setAlarm($WED, 14, 14);
    # setAlarm($WED, 14, 29);
    # dentist Tue 30 Jun 20
    # setAlarm($TUE, 14, 44);
    # setAlarm($TUE, 14, 59);
    # prodops
    # setAlarm($TUE, 9, 44);
    # company meeting
    # setAlarm($TUE, 8, 44);
    # satellite bonus is over
    # setAlarm(0, 7, 58);
    # setAlarm(1, 7, 58);
    # setAlarm(2, 7, 58);
    # setAlarm(3, 7, 58);
    # setAlarm(4, 7, 58);
    # setAlarm(5, 7, 58);
    # setAlarm(6, 7, 58);
    # virtual user summit walk through
    # setAlarm($TUE, 9, 44);
    # company meeting 200331
    # setAlarm($MON, 8, 44);
    # prodops 200408
    # setAlarm($WED, 9, 44);
    # dev 200408
    # setAlarm($WED, 11, 44);
    # company meeting 200331
    # setAlarm($WED, 9, 44);
    # setAlarm($MON, 17, 0);
    # setAlarm($FRI, 3, 0);
    # dentist
    # setAlarm($MON, 13, 0);
    # setAlarm($MON, 13, 30);
    # setAlarm($MON, 13, 45);
    # setAlarm($MON, 14, 0);
    # setAlarm($WED, 10, 45);
    # setAlarm($WED, 11, 0);
    # setAlarm($WED, 11, 15);
    # setAlarm($WED, 11, 30);
    # setAlarm($WED, 9, 0);
    # setAlarm($SUN, 11, 0);
    # interview
    # setAlarm($WED, 14, 0);
    # company meeting 6 Nov 19
    # setAlarm($WED, 10, 44);
    # Jiao He interview 	meet.google.com/adx-eebe-cqn
    # setAlarm($FRI, 15, 45);
    # setAlarm($THU, 14, 0);
    # setAlarm($TUE, 12, 45);
    # company meeting
    # setAlarm($MON, 11, 44);
    # dentist 190724
    # setAlarm($WED, 11, 0);
    # setAlarm($WED, 11, 30);
    # setAlarm($WED, 12, 0);
    # setAlarm($THU, 9, 0);
    # setAlarm($WED, 9, 0);
    # setAlarm($WED, 9, 30);
    # setAlarm($SUN, 16, 45);
    # setAlarm($SUN, 7, 0);
    # setAlarm($WED, 9, 44);
    # setAlarm($WED, 10, 44);
    # setAlarm($WED, 8, 14);
    # setAlarm($WED, 8, 44);
    # setAlarm($WED, 9, 14);
    # setAlarm($WED, 9, 44);
    # setAlarm($SUN, 7, 0);
    # setAlarm($MON, 20, 0);
    # setAlarm($TUE, 9, 15);
    # setAlarm($WED, 9, 14);
    # setAlarm($WED, 8, 44);
    # setAlarm($THU, 10, 0);
    # setAlarm($THU, 12, 29);
    # setAlarm($THU, 17, 0);
    # setAlarm($THU, 18, 14);
    # setAlarm($FRI, 5, 44);
    # setAlarm($SAT, 8, 45);
    # setAlarm($SAT, 10, 15);
    # DST
    # setAlarm($WED, 14, 14);
    # setAlarm($WED, 15, 14);
    # setAlarm($WED, 16, 14);
    # setAlarm($WED, 17, 14);
    # setAlarm($WED, 18, 14);
    # setAlarm($WED, 19, 14);
    # standard time
    # setAlarm($WED, 18, 14);
    # setAlarm($THU, 8, 14);
    # Howard Lin
    # setAlarm($TUE, 15, 44);
    # Oxana
    # setAlarm($FRI, 18, 44);
    # interview review
    # setAlarm($THU, 12, 44);
    # interview review
    # setAlarm($TUE, 10, 44);
    # next interview  Mike Afandi
    # setAlarm($WED, 14, 44);
    # company meeting
    # setAlarm($THU, 8, 44);
    # interview
    # setAlarm($THU, 14, 44);
    # wednesday build meeting
    # setAlarm($WED, 12, 14);
    # tuesday meeting after MLK
    # setAlarm($TUE, 8, 44);
    # dentist
    # setAlarm($MON, 11, 00);
    # star probably as dark as it gets at 6:20, should set within the hour or so
    # setAlarm($MON, 17, 15);
    # setAlarm($MON, 17, 25);
    # first saw it at 5:27pm
    # setAlarm($MON, 17, 35);
    # first saw second star at 5:40pm
    # setAlarm($MON, 17, 55);
    # setAlarm($MON, 18, 15);
    # intervu Aman
    # setAlarm($WED, 16, 0);
    # setAlarm($WED, 16, 15);
    # QE moved to Tue this week
    # setAlarm($TUE, 8, 44);
    # vax
    # setAlarm($TUE, 15, 59, "covid");
    # setAlarm($TUE, 16, 44, "covid");
    # dentist
    # setAlarm($MON, 13, 15, "dentist 210405");
    # company meeting
    # setAlarm($THU, 8, 44, "company meeting");
    # FJ to dealer
    # setAlarm($WED, 11, 0, "FJ to dealer");
    # checkout
    # setAlarm($THU, 11, 0, "check out time");
}

sub isRunning
{
    my @lines = `ps -ela`;
    my $count = 0;
    for my $line (@lines)
    {
        if ($line =~ /reminders.plx/)
        {
            print "\n$line\n";
            $count++;
        }
    }
    if ($count > 1)
    {
        print "\nexiting\n";
        exit(1);
    }
    $count = 0;
    @lines = `ps -alef`;
    for my $line (@lines)
    {
        if ($line =~ /reminders.plx/)
        {
            print "\n$line\n";
            $count++;
        }
    }
    if ($count > 1)
    {
        print "\nexiting\n";
        exit(1);
    }
}

sub setAlarm
{
    my ($wday, $hour, $min, $msg) = @_;
    print "setting alarm $wday, $hour, $min for $msg\n";
    my %alarm;
    $alarm{'wday'} = $wday;
    $alarm{'hour'} = $hour;
    $alarm{'min'} = $min;
    $alarm{'msg'} = $msg;
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
        my $amsg = $hash{'msg'};
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
            print "first alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
        }
        if ($min == $amin + 5 && ($sec == 0 || $sec == 5 || $sec == 10 || $sec == 15 || $sec == 20 || $sec == 25 || $sec == 30))
        {
            print "second alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
            sleep(1);
            print "second alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
        }
        if ($min == $amin + 10 && ($sec == 0 || $sec == 5 || $sec == 10 || $sec == 15 || $sec == 20 || $sec == 25 || $sec == 30 || $sec == 35 || $sec == 40 || $sec == 45))
        {
            print "third  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
            sleep(1);
            print "third  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
            sleep(1);
            print "third  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
        }
        if ($min >= $amin + 15 && $sec % 5 == 0)
        {
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
            sleep(1);
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
            sleep(1);
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
            sleep(1);
            print "YOU'RE  LATE  alarm  $awday $ahour $amin at $tag wday = $wday $shour $smin $sec $amsg\n";
        }
    }
}

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

main();
