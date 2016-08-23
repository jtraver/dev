#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    my $str1 = "a string that has a certain length longer than the length I would prefer it to have";
    my $len1 = length($str1);
    print "$len1\n";
    my $offset = 0;
    my $len2 = 80;
    print "$str1\n";
    my $str2 = substr($str1, $offset, $len2);
    print "$str2\n";
    my $len3 = 90;
    my $str3 = substr($str1, $offset, $len3);
    print "$str3\n";
}

main();
