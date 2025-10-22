#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use Time::Local;

sub makeDateTagMin 
{
    # my $now = time;
    my ($now) = @_;
    print "now is $now\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($now);
    $year -= 100;   
    $mon++;         
    # my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    my $tag = sprintf("%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min);
    # my $tag = sprintf("%02d%02d%02d", $year, $mon, $mday);
    return $tag;    
}             


sub makeDateTagSec 
{
    # my $now = time;
    my ($now) = @_;
    print "now is $now\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($now);
    $year -= 100;   
    $mon++;         
    my $tag = sprintf("%02d%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min, $sec);
    # my $tag = sprintf("%02d%02d%02d%02d%02d", $year, $mon, $mday, $hour, $min);
    # my $tag = sprintf("%02d%02d%02d", $year, $mon, $mday);
    return $tag;    
}             

sub main
{
    my $time0 = time;
    # my $tag = makeDateTagMin($time0);
    my $tag = makeDateTagSec($time0);
    print "$tag\n";
    my $time1 = parseDateTime($tag);
    my $diff1 = $time0 - $time1;
    print "$tag -> $diff1 seconds before $tag\n";
    # my $str2 = "Sep 19 2017 00:08:15 GMT:";
    # my $str2 = "Sep 18 2017 21:40:27 GMT:";
    my $str2 = "Sep 19 2017 00:45:33 GMT:";
    my $time2 = parseDateTime($str2);
    my $diff2 = $time0 - $time2;
    print "$str2 -> $diff2 seconds before $tag\n";
    # my $str3 = "Mon Sep 18 20:47:24 EDT 2017";

    my $str3 = "Mon Sep 18 21:05:49 EDT 2017";
    my $time3 = parseDateTime($str3);
    my $diff3 = $time0 - $time3;
    print "$str3 -> $diff3 seconds before $tag\n";

    my $str4 = "10 Mar 21 21:13 EST";
    my $time4 = parseDateTime($str4);
    my $diff4 = $time0 - $time4;
    print "$str4 -> $diff4 seconds before $tag\n";

    check_log_times();
}

#use DateTime::Format::Strptime;
#
#my $parser = DateTime::Format::Strptime->new(
#  pattern => '%B %d, %Y %I:%M %p %Z',
#  on_error => 'croak',
#);
#
#my $dt = $parser->parse_datetime('October 28, 2011 9:00 PM PDT');
#
#print "$dt\n";



# https://stackoverflow.com/questions/7486470/how-to-parse-a-string-into-a-datetime-object-in-perl
# use Date::Parse;
#use DateTime;
#
#my $str = "Tue, 20 Sep 2011 08:51:08 -0500";
#my $epoch = str2time($str);
#my $datetime = DateTime->from_epoch(epoch => $epoch);


# http://www.perlmonks.org/?node_id=769091
#use strict;
#use Time::Local;
#
#for my $date ("06/06/2009",'01/30/09') {
#    my ($m,$d,$y) = $date =~ m|(\d+)/(\d+)/(\d+)|;
#    my $timet = timelocal(0, 0, 0, $d, $m, $y);
#    print "Date '$date' => $timet\n";
#    print "localtime($timet): ", scalar localtime $timet, "\n";
#}


# http://perldoc.perl.org/Time/Local.html
# use Time::Local;
# my $time = timelocal( $sec, $min, $hour, $mday, $mon, $year );
# my $time = timegm( $sec, $min, $hour, $mday, $mon, $year );
#


my %months;
$months{"Jan"} = 0;
$months{"Feb"} = 1;
$months{"Mar"} = 2;
$months{"Apr"} = 3;
$months{"May"} = 4;
$months{"Jun"} = 5;
$months{"Jul"} = 6;
$months{"Aug"} = 7;
$months{"Sep"} = 8;
$months{"Oct"} = 9;
$months{"Nov"} = 10;
$months{"Dec"} = 11;

sub parseDateTime
{
    print "\nparseDateTime\n";
    my ($dateTime) = @_;
    print "$dateTime\n";
    my $returnTime = -1;
    # Sep 19 2017 00:08:15 GMT:
    if ($dateTime =~ /(\S+) (\d+) (\d+) (\d+):(\d+):(\d+) GMT:/)
    {
        my $monStr = $1;
        my $mon = $months{$monStr};
        my $mday = $2;
        my $year = $3;
        my $hour = $4;
        my $min = $5;
        my $sec = $6;
        print "$sec, $min, $hour, $mday, $monStr, $year\n";
        print "$sec, $min, $hour, $mday, $mon, $year\n";
        $returnTime = timegm($sec, $min, $hour, $mday, $mon, $year);
        print "1 time is $returnTime\n";
    }
    # Mon Sep 18 20:47:24 EDT 2017
    elsif ($dateTime =~ /(\S+) (\S+) (\d+) (\d+):(\d+):(\d+) (\S+) (\d+)/)
    {
        my $dowStr = $1;
        my $monStr = $2;
        my $mon = $months{$monStr};
        my $mday = $3;
        my $hour = $4;
        my $min = $5;
        my $sec = $6;
        my $tzStr = $7;
        my $year = $8;
        print "$sec, $min, $hour, $mday, $monStr, $year\n";
        print "$sec, $min, $hour, $mday, $mon, $year\n";
        $returnTime = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "2 time is $returnTime\n";
    }
    elsif ($dateTime =~ /(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)/)
    {
        my $year = $1;
        my $mon = $2 - 1;
        my $mday = $3;
        my $hour = $4;
        my $min = $5;
        my $sec = $6;
        print "$sec, $min, $hour, $mday, $mon, $year\n";
        $returnTime = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "3 time is $returnTime\n";
    }
    # 1709182030
    elsif ($dateTime =~ /(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)/)
    {
        my $year = $1;
        my $mon = $2 - 1;
        my $mday = $3;
        my $hour = $4;
        my $min = $5;
        my $sec = 0;
        print "$sec, $min, $hour, $mday, $mon, $year\n";
        $returnTime = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "4 time is $returnTime\n";
    }
    # my $str4 = "10 Mar 21 21:13 EST";
    elsif ($dateTime =~ /(\d\d) (\S\S\S) (\d\d) (\d\d):(\d\d) (\S\S\S)/)
    {
        my $mday = $1;
        my $monStr = $2;
        my $mon = $months{$monStr};
        my $year = $3 + 2000;
        my $hour = $4;
        my $min = $5;
        my $tzStr = $6;
        # my $year = $1;
        # my $mon = $2 - 1;
        # my $mday = $3;
        # my $hour = $4;
        # my $min = $5;
        # my $sec = 0;
        my $sec = 0;
        print "$sec, $min, $hour, $mday, $mon, $year\n";
        $returnTime = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "5 time is $returnTime\n";
    }
    # Sep 19 2017 00:08:15 GMT:
    # WHAT: Oct 22 2025 16:16:19 GMT
    elsif ($dateTime =~ /(\S+) (\d+) (\d+) (\d+):(\d+):(\d+) GMT/)
    {
        print "aerospike server logs $dateTime\n";
        my $monStr = $1;
        my $mon = $months{$monStr};
        my $mday = $2;
        my $year = $3;
        my $hour = $4;
        my $min = $5;
        my $sec = $6;
        print "str $sec, $min, $hour, $mday, $monStr, $year\n";
        print "int $sec, $min, $hour, $mday, $mon, $year\n";
        $returnTime = timegm($sec, $min, $hour, $mday, $mon, $year);
        print "6 time is $returnTime\n";
    }
    # WHAT: Oct 22 09:16
    elsif ($dateTime =~ /(\S+) (\d+) (\d+):(\d+)/)
    {
        print "ls -lat $dateTime\n";
        my $monStr = $1;
        my $mon = $months{$monStr};
        my $mday = $2;
        my $hour = $3;
        my $min = $4;
        my $now1 = time;
        print "now1 is $now1\n";
        my ($sec,$min1,$hour1,$mday1,$mon1,$year,$wday,$yday,$isdst) = localtime($now1);
        # $sec does not matter -> it will be off 0-59 randomly no matter what it is set to
        $year -= 100;   
        $year += 2000;
        print "year is $year\n";
        print "$min, $hour, $mday, $monStr\n";
        print "$min, $hour, $mday, $mon\n";
        $returnTime = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "7 time is $returnTime\n";
    }
    else
    {
        print "WHAT: $dateTime\n";
    }
# my $time = timelocal( $sec, $min, $hour, $mday, $mon, $year );
# my $time = timegm( $sec, $min, $hour, $mday, $mon, $year );
    return $returnTime;
}


# CAUSE Oct 22 2025 16:16:19 GMT: WARNING (as): (signal.c:247) SIGSEGV received, aborting Aerospike Enterprise Edition build 8.1.1.0-start-48-g9ec5aeb os el9 arch x86_64 sha 9ec5aeb ee-sha fb39788
# sscLine -rw-r-----. 1 root root 1192831873 Oct 22 09:16 /var/lib/systemd/coredump/core.asd.0.a8c472bceeb446e29f5868c7ee49af65.2296041.1761149780000000.zst
sub check_log_times
{
    my $now0 = time;
    my $date0 = makeDateTagSec($now0);
    print "\nSTART check_log_times\n";
    print "now0 is $now0\n";
    print "date0 = $date0\n";
    my $time0 = parseDateTime($date0);
    print "time0 = $time0\n";
    my $line1 = "CAUSE Oct 22 2025 16:16:19 GMT: WARNING (as): (signal.c:247) SIGSEGV received, aborting Aerospike Enterprise Edition build 8.1.1.0-start-48-g9ec5aeb os el9 arch x86_64 sha 9ec5aeb ee-sha fb39788";
    # my $line1 = "CAUSE Oct 22 2025 17:16:19 GMT: WARNING (as): (signal.c:247) SIGSEGV received, aborting Aerospike Enterprise Edition build 8.1.1.0-start-48-g9ec5aeb os el9 arch x86_64 sha 9ec5aeb ee-sha fb39788";
    # PDT my $line2 = "sscLine -rw-r-----. 1 root root 1192831873 Oct 22 09:16 /var/lib/systemd/coredump/core.asd.0.a8c472bceeb446e29f5868c7ee49af65.2296041.1761149780000000.zst";
    # MDT
    my $line2 = "sscLine -rw-r-----. 1 root root 1192831873 Oct 22 10:16 /var/lib/systemd/coredump/core.asd.0.a8c472bceeb446e29f5868c7ee49af65.2296041.1761149780000000.zst";
    my $date1 = $line1;
    $date1 =~ s/^CAUSE (.*): WARNING.*$/$1/;
    print "date1 = $date1\n";
    my @date2 = split(" ", $line2);
    my $date2 = "$date2[6] $date2[7] $date2[8]";
    my $time1 = parseDateTime($date1);
    print "time1 = $time1\n";
    print "date2 = $date2\n";
    my $time2 = parseDateTime($date2);
    print "now0 = $now0\n";
    print "time0 = $time0\n";
    print "time1 = $time1\n";
    print "time2 = $time2\n";
    print "date0 = $date0\n";
    print "date1 = $date1\n";
    print "date2 = $date2\n";
    my $diff0 = $now0 - $time0;
    my $diff1 = $now0 - $time1;
    my $diff2 = $now0 - $time2;
    print "diff0 = $diff0\n";
    print "diff1 = $diff1\n";
    print "diff2 = $diff2\n";
    print "END check_log_times\n";
}

main();
