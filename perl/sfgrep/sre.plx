#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use File::Find;

$| = 1;
my $status = 800;
my $count = 0;
my $output = "TextFiles.txt";
my @files;
my $search_word = shift;
if (!defined($search_word) || $search_word eq "")
{
        die "need a word to search for";
}
my $replace_word = shift;
if (!defined($replace_word) || $replace_word eq "")
{
        die "need a word to replace with";
}

sub wanted
{
        $count++;
        if ($count % $status == 0)
        {
                print ".";
        }
        my $name = $File::Find::name;
        if (! -d && -T &&
                $name !~ /\/SFGREP\// &&
                $name !~ /\/coverity\// &&
                $name !~ /\/branches\// &&
                $name !~ /\/tags\// &&
                $name !~ /\/FGREP\// &&
                $name !~ /\/yala\// &&
                $name !~ /\/\.git\// &&
                $name !~ /\/\.svn\// &&
                $name !~ /\/CVS\// &&
                $name !~ /\/logs\// &&
                $name !~ /\/FreeBSD.4.11.package\// &&
                $name !~ /\/rhel.4.3.package\// &&
                $name !~ /\/rhel.4.4.package\//)
        {
                # print "$name\n";
                $files[@files] = $name;
        }
}

sub search_replace
{
        # open(OUTPUT, ">$output") or die "Can't write $output: $!";
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
                        if ($line =~ /$search_word/i)
                        {
                                $/ = $save_rs;
                                $file_open = open(FILE, $file);
                                if ($file_open)
                                {
                                        my @lines = <FILE>;
                                        close(FILE);
                                        chomp(@lines);
                                        $file_open = open(FILE, ">$file");
                                        if ($file_open)
                                        {
                                            foreach $line (@lines)
                                            {
                                                    if ($line =~ /$search_word/i)
                                                    {
                                                            $line =~ s/$search_word/$replace_word/;
                                                            print FILE "$line\n";
                                                    }
                                                    else
                                                    {
                                                            print FILE "$line\n";
                                                    }
                                            }
                                            close(FILE);
                                        }
                                        else
                                        {
                                            print "coud not write $file: $!";
                                            print "\n";
                                        }
                                }
                                else
                                {
                                        print "coud not read $file in line mode: $!";
                                        print "\n";
                                }
                        }
                }
                else
                {
                        print "Can't read file $file: $!";
                        print "\n";
                }
        }
}

sub main
{
    open(OUTPUT, ">$output") or die "Can't write $output: $!";
    File::Find::find(\&wanted, "..");
    close(OUTPUT);
    print "\n";
    search_replace
}

main();
