#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    make_gif_html_pages();
}

sub make_gif_html_pages
{
    my $dir = "gif_html";
    mkdir $dir;
    my $glob = "*.gif";
    my @glob = glob($glob);
    chomp(@glob);
    print "<ol>\n";
    foreach my $file (@glob)
    {
        my $filename = "$dir/$file.html";
        my $fileopen = open(FILE, ">$filename");
        print "<li><a href=\"$filename\">$file<\/>\n";
        print FILE "<img height=600 width=600 src=\"../$file\">\n";
        close(FILE);
    }
}

main();
