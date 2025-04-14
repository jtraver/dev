#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $status = 1;
my @files;
my $count = 0;

my $line_limit = 20000;

$| = 1;
my $word = shift;
if (!defined($word) || $word eq "")
{
        die "need a word to search for";
}
mkdir "FGREP";
my $output = "FGREP/$word.txt";
if (-e $output)
{
}
else
{
        open(OUTPUT, ">$output") or die "Can't write $output: $!";
        load_files();
        my $save_rs = $/;
        my $skipped_lines = 0;
        my $skipped_files = 0;
        foreach my $file (sort @files)
        {
                if ($file =~ /FreeBSD.4.11.package/ || $file =~ /rhel.4.3.package/)
                {
                        next;
                }
                $count++;
                if ($count % $status == 0)
                {
                        print ".";
                }
                $/ = undef;     # whole file mode
                my $file_open = open(FILE, $file);
                if ($file_open)
                {
                        my $line = <FILE>;      # whole file
                        close(FILE);
                        if ($line =~ /$word/i)
                        {
                                print OUTPUT
"---------------------------------------------------------------------------\n";
                                print OUTPUT
"---------------------------------------------------------------------------\n";
                                print OUTPUT "| $file\n";
                                print OUTPUT
"---------------------------------------------------------------------------\n";
                                $/ = $save_rs;
                                $file_open = open(FILE, $file);
                                if ($file_open)
                                {
                                        my @lines = <FILE>;
                                        close(FILE);
                                        chomp(@lines);
                                        my $skipped = 0;
                                        foreach $line (@lines)
                                        {
                                            my $len1 = length($line);
                                            if ($len1 > $line_limit)
                                            {
                                                # print STDERR "line length is $len1 for $file\n";
                                                $skipped++;
                                                next;
                                            }
                                                if ($line =~ /$word/i)
                                                {
                                                        print OUTPUT "\t$line\n";
                                                }
                                        }
                                        if ($skipped > 0)
                                        {
                                            $skipped_lines += $skipped;
                                            $skipped_files++;
                                        }
                                }
                                else
                                {
                                        print "coud not read $file in line mode: $!";
                                        print "\n";
                                }
                                print OUTPUT "\n";
                        }
                }
                else
                {
                        print "Can't read file $file: $!";
                        print "\n";
                }
        }
        if ($skipped_lines > 0)
        {
            print STDERR "WARNING: skipped $skipped_lines in $skipped_files because of line limit $line_limit\n";
        }
        close(OUTPUT);
        print "\n";
}
my $cmd = "vi \"$output\"";
system($cmd);
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
