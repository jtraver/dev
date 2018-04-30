#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;


sub stat_file
{
    my ($filename) = @_;
    print "\n---------------------------------------------------------------------------------\n";
    print "$filename\n";
    my ($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,$atime,$mtime,$ctime,$blksize,$blocks) = stat($filename);
    print "$filename: dev = $dev\n";
    print "$filename: ino = $ino\n";
    print "$filename: mode = $mode\n";
    print "$filename: nlink = $nlink\n";
    print "$filename: uid = $uid\n";
    print "$filename: gid = $gid\n";
    print "$filename: rdev = $rdev\n";
    print "$filename: size = $size\n";
    print "$filename: atime = $atime\n";
    print "$filename: mtime = $mtime\n";
    print "$filename: ctime = $ctime\n";
    print "$filename: blksize = $blksize\n";
    print "$filename: blocks = $blocks\n";

    my $time = time;
    print "\ntime = $time\n";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($time);
    $year -= 100;
    my $tag = sprintf("%02d%02d%02d%02d%02d.%02d", $year, $mon, $mday, $hour, $min, $sec);
    print "$time: tag = $tag\n";
    my $diff;
    my $hours;
    my $days;

    print "\nmtime\n";
    ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($mtime);
    $year -= 100;
    $tag = sprintf("%02d%02d%02d%02d%02d.%02d", $year, $mon, $mday, $hour, $min, $sec);
    print "$mtime: tag = $tag\n";
    $diff = $time - $mtime;
    print "$mtime: diff = $diff\n";
    $hours = int($diff / 3600);
    $hours += 1;
    print "$mtime: hours = $hours\n";
    $days = $hours / 24;
    print "$mtime: days = $days\n";


    print "\nctime\n";
    ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($ctime);
    $year -= 100;
    $tag = sprintf("%02d%02d%02d%02d%02d.%02d", $year, $mon, $mday, $hour, $min, $sec);
    print "$ctime: tag = $tag\n";
    $diff = $time - $ctime;
    print "$ctime: diff = $diff\n";
    $hours = int($diff / 3600);
    $hours += 1;
    print "$ctime: hours = $hours\n";
    $days = $hours / 24;
    print "$ctime: days = $days\n";


    print "\natime\n";
    ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($atime);
    $year -= 100;
    $tag = sprintf("%02d%02d%02d%02d%02d.%02d", $year, $mon, $mday, $hour, $min, $sec);
    print "$atime: tag = $tag\n";
    $diff = $time - $atime;
    print "$atime: diff = $diff\n";
    $hours = int($diff / 3600);
    $hours += 1;
    print "$atime: hours = $hours\n";
    $days = $hours / 24;
    print "$atime: days = $days\n";

# my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($time);
# my $tag = sprintf("%02d%02d%02d%02d.%02d", $mon, $mday, $hour, $min, $sec);
}

sub main
{
    stat_file("stat1.plx");
    stat_file("stat2.plx");
}

main();
