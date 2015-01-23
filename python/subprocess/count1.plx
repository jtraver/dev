#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

for (my $i1 = 0; $i1 < 1000; $i1++)
{
    my $time = time;
    print "$time\n";
    sleep(1);
}
