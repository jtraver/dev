#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# https://rosettacode.org/wiki/Check_output_device_is_a_terminal#Perl
#$ perl -e "warn -t STDOUT ? 'Terminal' : 'Other'"
#Terminal
#$ perl -e "warn -t STDOUT ? 'Terminal' : 'Other'" > x.tmp
#Other

warn -t STDOUT ? 'STDOUT Terminal' : 'STDOUT Other';
warn -t STDERR ? 'STDERR Terminal' : 'STDERR Other';

my $out1 = -t STDOUT;
my $err1 = -t STDERR;

print "stdout is $out1\n";
print "stderr is $err1\n";

my $istty = 0;
if (-t STDOUT)
{
    $istty = 1;
}

if ($istty == 1)
{
    print "stdout is to a terminal\n";
}
else
{
    print "stdout is not to a terminal\n";
}

if ($out1)
{
    print "STDOUT is Terminal\n";
}
else
{
    print "STDOUT is Other\n";
}

if ($err1)
{
    print "STDERR is Terminal\n";
}
else
{
    print "STDERR is Other\n";
}


