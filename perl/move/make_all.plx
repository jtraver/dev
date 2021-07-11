#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    make_all();
}

sub make_all
{
    my @glob = `find .`;
    chomp(@glob);
    print "<ol>\n";
    my $count = 0;
    my $fileopen = open(INDEX, ">index.html");
    foreach my $file (sort @glob)
    {
        if (-d $file)
        {
            next;
        }
        if ($count % 50 == 0)
        {
            if ($count != 0)
            {
                print OUTPUT "</ol>\n";
                close(OUTPUT);
            }
            $count++;
            my $filen = "$count.html";
            my $fileopen = open(OUTPUT, ">$filen");
            print INDEX "<li><a href=\"$filen\">$filen<\/>\n";
            print OUTPUT "<ol>\n";
        }
        else
        {
            $count++;
        }
        # my $filename = "$dir/$file.html";
        # my $fileopen = open(FILE, ">$filename");
        # print "<li><a href=\"$filename\">$file<\/>\n";
        print OUTPUT "<li><a href=\"$file\">$file<\/></br>\n";
        print OUTPUT "<img height=1000 width=1000 src=\"$file\">\n";
        # print OUTPUT "<img height=300 width=300 src=\"$file\">\n";
        # print FILE "<img height=100 width=100 src=\"$file\">\n";
        # close(FILE);
    }
    print "</ol>\n";
}

main();
