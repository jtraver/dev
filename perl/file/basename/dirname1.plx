#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use File::Basename;

my @suffixlist;
$suffixlist[@suffixlist] = '.data';
$suffixlist[@suffixlist] = '.out';
$suffixlist[@suffixlist] = '.plx';
$suffixlist[@suffixlist] = '.tmp';
$suffixlist[@suffixlist] = '.txt';

my @files = `find ../..`;
chomp(@files);
my %suffixes;
foreach my $file (@files)
{
    print "$file\n";
    my ($name, $path, $suffix) = fileparse($file, @suffixlist);
    my $dirname = dirname($file);
    my $basename = basename($file);
    print "  name $name\n";
    print "  path $path\n";
    print "  dirname $dirname\n";
    print "  basename $basename\n";
    print "  suffix $suffix\n";
    if ($suffix eq '' && $name =~ /\./ && $name ne '..')
    {
        $suffixes{$name}++
    }
}
foreach my $suffix (sort keys %suffixes)
{
    print "missing suffix for $suffix\n";
}
