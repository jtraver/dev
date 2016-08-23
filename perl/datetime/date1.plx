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
}

main();
