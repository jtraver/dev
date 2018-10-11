#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# trim $line =~ s/^\s+//; $line =~ s/\s+$//;
# $line =~ s/^\s+//;
# $line =~ s/\s+$//;

sub main
{

    my $files1 = `ls ..`;
    my @fields1 = split("\n", $files1);
    for my $field1 (@fields1)
    {
        print "field1 $field1\n";
    }
    my @files2 = `ls ..`;
    for my $file2 (@files2)
    {
        # trim
        $file2 =~ s/^\s+//;
        $file2 =~ s/\s+$//;
        print "file2 = $file2\n";
    }

    my $branches1 = `git branch -a`;
    @fields1 = split("\n", $branches1);
    for my $field1 (@fields1)
    {
        # trim
        $field1 =~ s/^\s+//;
        $field1 =~ s/\s+$//;
        print "field1 $field1\n";
    }
    my @branches2 = `git branch -a`;
    for my $branch2 (@branches2)
    {
        # trim
        $branch2 =~ s/^\s+//;
        $branch2 =~ s/\s+$//;
        print "branch2 = $branch2\n";
    }


}

main();
