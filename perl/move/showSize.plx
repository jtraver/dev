#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use File::Find;

my %files;
my $status = 100;
my $count = 0;

sub wanted
{
        $count++;
        if ($count % $status == 0)
        {
                print ".";
        }
        my $name = $File::Find::name;
        my $size = -s;
        if (defined($size))
        {
            print "$size $name\n";
            $files{$name} = $size;
        }
        else
        {
            print "$name\n";
        }
}

my $output = "FileSize.txt";
File::Find::find(\&wanted, ".");
open(OUTPUT, ">$output") or die "Can't write $output: $!";
for my $file (sort {$files{$b} <=> $files{$a}} keys %files)
{
    my $size = $files{$file};
    print OUTPUT "$size $file\n";
}
close(OUTPUT);
print "\n";
