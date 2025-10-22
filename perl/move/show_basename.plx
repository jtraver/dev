#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use File::Basename;

sub main
{
    show_basename();
}

sub show_basename
{
    my @glob = `find .`;
    foreach my $filename (@glob)
    {
        my $dir2 = File::Basename::dirname($filename);
        my $basename2 = basename($filename);
        print "$basename2\n";
    }
}

main();
