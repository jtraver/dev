#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# trim $line =~ s/^\s+//; $line =~ s/\s+$//;
# $line =~ s/^\s+//;
# $line =~ s/\s+$//;
# $line =~ s/\s+/ /g; # trim all interior white space as well

# $line =~ s/\s+/ /g; # trim all interior white space as well

sub main
{
    do_split('asyncload3@async/asbench:ref=test-ready');
    do_split("asyncload3\@async/asbench:ref=test-ready");
    my $filename = "data1.txt";
    my $fileopen = open(DATA, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        exit 1;
    }
    my @lines = <DATA>;
    close(DATA);
    chomp(@lines);
    for my $line (@lines)
    {
        do_split($line);
    }
    exit 0;
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

sub do_split
{
    my ($str1) = @_;
    print "\ndo_split\n";
    print "  str1 = $str1\n";
    my $str2 = $str1;
    $str2 =~ tr/@/ /s;
    print "  str2 = $str2\n";
    print "  str1 = $str1\n";
    my @fields1 = split("@", $str1);
    print "  fields1 = @fields1\n";
    my $len1 = @fields1;
    print "  len(fields1) = $len1\n";
}

main();
