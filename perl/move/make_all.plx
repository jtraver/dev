#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $prefix = "k";

sub main
{
    make_all();
}

sub make_all
{
    my @glob = `find .`;
    chomp(@glob);
    # print "<ol>\n";
    my $count = 0;
    my $fileopen = open(INDEX, ">index.html");
    foreach my $file (sort @glob)
    {
        if (-d $file)
        {
            next;
        }
        if ($file =~ /\.sh$/)
        {
            next;
        }
        if ($file =~ /mk.dir/)
        {
            next;
        }
        if ($file =~ /\.\/miss/)
        {
            next;
        }
        if ($file =~ /\.out$/)
        {
            next;
        }
        if ($file =~ /\.tmp$/)
        {
            next;
        }
        if ($file =~ /\.svg$/)
        {
            next;
        }
        if ($file =~ /\.txt$/)
        {
            next;
        }
        if ($file =~ /\.html$/)
        {
            next;
        }
        if ($file =~ /\.plx$/)
        {
            next;
        }
        if ($file =~ /.DS_Store/)
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
            my $filen = "$prefix$count.html";
            my $fileopen = open(OUTPUT, ">$filen");
            print INDEX "<li><a href=\"$filen\">$filen $file<\/>\n";
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
        # print OUTPUT "<img height=1000 width=1000 src=\"$file\">\n";
        # 240301 print OUTPUT "<img height=800 width=800 src=\"$file\">\n";
        print OUTPUT "<img height=800 width=800 src=\"$file\">\n";
        # print OUTPUT "<img height=400 width=400 src=\"$file\">\n";
        # print OUTPUT "<img height=300 width=300 src=\"$file\">\n";
        # print FILE "<img height=100 width=100 src=\"$file\">\n";
        # close(FILE);
    }
    close(INDEX);
    # print "</ol>\n";
}

main();
