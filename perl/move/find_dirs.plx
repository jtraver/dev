#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

sub main
{
    # make_gif_html_pages();
    find_dirs();
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

sub find_dirs
{
    my $glob = "*";
    my @glob = glob($glob);
    foreach my $filename (@glob)
    {
        if (-d $filename)
        {
            # print "$filename is a dir\n";
            my $labeled = "$filename/labeled.html";
            if (-e $labeled)
            {
                # print "$labeled exists\n";
            }
            else
            {
                print "$labeled does not exist\n";
            }
        }
    }
}

main();
