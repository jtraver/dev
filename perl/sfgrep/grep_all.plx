#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $status = 1;
my $count = 0;

my $line_limit = 20000;

$| = 1;
my $word = shift;
if (!defined($word) || $word eq "")
{
        die "need a word to search for";
}

my @strings;
my $strings;
my $count;
my @files = `find ..`;
$count = 0;
chomp(@files);
my %found;
foreach my $file (sort @files)
{
    # print "$file\n";
    my @lines = `grep -lia $word $file`;
    chomp(@lines);
    #foreach my $line (@lines)
    #{
    #    print "$file $line\n";
    #}
    my $match = $lines[0];
    if (defined($match))
    {
        print "MATCH file $file, match $match\n";
        $found{$count} = $file;
        $strings[$count] = "strings.$count";
        system("strings $file > strings.$count");
        $count++;
    }
}
print "show matching files\n";
foreach my $count1 (sort keys %found)
{
    my $strings = $strings[$count1];
    print "count1 = $count1\n";
    my $file1 = $found{$count1};
    print "$count1 $file1 $strings\n";
    system("grep -ia $word $strings");
}
print "DONE\n";


##!/usr/bin/perl
#use strict;
#use warnings;
#use Data::Dumper;
#
## The null character can be represented as '\0' within double quotes
#my $null_char = "\0";
#
## Create a sample string with null characters
#my $string = "field1" . $null_char . "field2" . $null_char . "field3";
#
## Split the string using the null character as the delimiter
#my @fields = split /\0/, $string;
#
## Print the resulting array elements to verify the split
#print Dumper \@fields;
#
