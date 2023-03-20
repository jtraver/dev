#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $home = $ENV{"HOME"};
print "home is $home\n";

# file/stat1.plx:    my @glob = glob("*");
# file/stat1.plx:    foreach my $file (@glob)

my @glob = glob("$home/*");
foreach my $file (@glob)
{
    print "$file\n";
}
