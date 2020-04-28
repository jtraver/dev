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

sub parse1_main
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
    my ($dateTime) = @_;
    print "$dateTime\n";
    my $time;
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
        $time = timegm($sec, $min, $hour, $mday, $mon, $year);
        print "time is $time\n";
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
        $time = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "time is $time\n";
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
        $time = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "time is $time\n";
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
        $time = timelocal($sec, $min, $hour, $mday, $mon, $year);
        print "time is $time\n";
    }
    else
    {
        print "WHAT: $dateTime\n";
    }
# my $time = timelocal( $sec, $min, $hour, $mday, $mon, $year );
# my $time = timegm( $sec, $min, $hour, $mday, $mon, $year );
    return $time;
}

my %daystr;
$daystr{0} = "Sun";
$daystr{1} = "Mon";
$daystr{2} = "Tue";
$daystr{3} = "Wed";
$daystr{4} = "Thu";
$daystr{5} = "Fri";
$daystr{6} = "Sat";

my %monstr;
$monstr{0} = "Jan";
$monstr{1} = "Feb";
$monstr{2} = "Mar";
$monstr{3} = "Apr";
$monstr{4} = "May";
$monstr{5} = "Jun";
$monstr{6} = "Jul";
$monstr{7} = "Aug";
$monstr{8} = "Sep";
$monstr{9} = "Oct";
$monstr{10} = "Nov";
$monstr{11} = "Dec";


sub show_date_from_time
{
    my ($when1, $time1) = @_;
    print "$when1 time is $time1\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($time1);
    my $full_year = $year + 1900;
    my $day_str = $daystr{$wday};
    my $mon_str = $monstr{$mon};
    # print "$wday $year $mon $mday $hour $min $sec\n";
    # print "$when1 date is $day_str $full_year $mon $mday $hour $min $sec\n";
    # print "$when1 date is $day_str $full_year $mday $mon_str $hour $min $sec\n";
    print "$when1 date is $day_str $mday $mon_str $full_year $hour $min $sec\n";
}

sub main
{
    my $now1 = time;

    print "time now is $now1\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($now1);
    my $full_year = $year + 1900;
    my $day_str = $daystr{$wday};
    # print "$wday $year $mon $mday $hour $min $sec\n";
    print "$day_str $full_year $mon $mday $hour $min $sec\n";
    show_date_from_time("now", $now1);

    my $min_secs = 60;
    my $hour_secs = $min_secs * 60;
    print "seconds in hour $hour_secs\n";
    my $day_secs = $hour_secs * 24;
    print "seconds in day $day_secs\n";
    my $week_secs = $day_secs * 7;
    print "seconds in week $week_secs\n";

    my $last_friday = 5 - $wday;
    if ($last_friday > 0)
    {
        $last_friday = $last_friday - 7;
    }
    my $last_friday_secs = $now1 + ($last_friday * $day_secs);
    show_date_from_time("last Friday ", $last_friday_secs);

    # my $lastweek1 = $now1 - $week_secs;
    my $lastweek1 = $last_friday_secs - $week_secs;
    show_date_from_time("one week ago", $lastweek1);
    # my $lastweek2 = $lastweek1 - $week_secs;
    my $weeks = 2;
    for (my $weeks = 2; $weeks < 20; $weeks++)
    {
        # my $lastweek2 = $now1 - ($week_secs * $weeks);
        my $lastweek2 = $last_friday_secs - ($week_secs * $weeks);
        show_date_from_time("$weeks weeks ago", $lastweek2);
    }

    # my $dowStr = $1;
    # my $monStr = $2;
    # my $mon = $months{$monStr};
    # my $mday = $3;
    # my $hour = $4;
    # my $min = $5;
    # my $sec = $6;
    # my $tzStr = $7;
    # my $year = $8;
    # print "$sec, $min, $hour, $mday, $monStr, $year\n";
    # print "$sec, $min, $hour, $mday, $mon, $year\n";
    # $time = timelocal($sec, $min, $hour, $mday, $mon, $year);
    # print "time is $time\n";
}

main();
