#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $status = 1;
my @files;
my $count = 0;
$| = 1;

my %exts;

sub load_files
{
        my $file = "TextFiles.txt";
        my $file_open = open(FILES, $file);
        if (!$file_open)
        {
                print STDERR "please run setTextFiles.plx\n";
                exit(1);
        }
        @files = <FILES>;
        close(FILES);
        chomp(@files);
        $status = @files / 79;
        if ($status <= 1)
        {
            $status = 1;
        }
}

load_files();

foreach my $file (sort @files)
{
    # print "$file\n";
    my @parts1 = split('/', $file);
    my $base = $parts1[@parts1 - 1];
    # print "$base\n";
    my @parts2 = split('\.', $base);
    my $ext = $parts2[@parts2 - 1];
    # print "$ext\n";
    $exts{$ext} += 1;
    if ($ext eq 'pl')
    {
        print "$file\n";
    }
}

foreach my $ext (sort keys %exts)
{
    my $val = $exts{$ext};
    print "$val $ext\n";
}
