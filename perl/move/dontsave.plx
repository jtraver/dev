#!/usr/bin/perl -w
use diagnostics;
use warnings;
use strict;
my $status = 1;
my @files;
my $count = 0;
$| = 1;
my $word = shift;
if (!defined($word) || $word eq "")
{
        die "need a word to search for";
}

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
my $save_rs = $/;
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
                        print STDOUT "\n";
                        print STDOUT "---------------------------------------------------------------------------\n";
                        print STDOUT "| $file\n";
                        print STDOUT "---------------------------------------------------------------------------\n";
                        $/ = $save_rs;
                        $file_open = open(FILE, $file);
                        if ($file_open)
                        {
                                my @lines = <FILE>;
                                close(FILE);
                                chomp(@lines);
                                foreach $line (@lines)
                                {
                                        if ($line =~ /$word/i)
                                        {
                                                print STDOUT "\t$line\n";
                                        }
                                }
                        }
                        else
                        {
                                print "coud not read $file in line mode: $!";
                                print "\n";
                        }
                        print STDOUT "---------------------------------------------------------------------------\n";
                        print STDOUT "\n";
                }
        }
        else
        {
                print "Can't read file $file: $!";
                print "\n";
        }
}
print "\n";
