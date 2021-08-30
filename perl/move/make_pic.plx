#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    make_html_pages();
}

sub make_html_pages
{
    my $glob = "*";
    my @glob = glob($glob);
    chomp(@glob);
    print "<ol>\n";
    foreach my $file (@glob)
    {
        print "<img src=\"$file\">\n";
    }
}

main();
