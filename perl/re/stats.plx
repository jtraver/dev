#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my %names;
my %songs;
my %countries;

sub stats
{
    print "\n";
    print "Names\n";
    foreach my $name (sort {$names{$b} <=> $names{$a}} keys %names)
    {
        my $count = $names{$name};
        print "$name $count\n";
    }
    print "\n";
    print "Songs\n";
    foreach my $song (sort {$songs{$b} <=> $songs{$a}} keys %songs)
    {
        my $count = $songs{$song};
        print "$song $count\n";
    }
    print "\n";
    print "Countries\n";
    foreach my $country (sort {$countries{$b} <=> $countries{$a}} keys %countries)
    {
        my $count = $countries{$country};
        print "$country $count\n";
    }
}

sub count
{
    my ($filename) = @_;
    print "$filename\n";
    my $fileopen = open(FILE, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    my @lines = <FILE>;
    close(FILE);
    chomp(@lines);
    foreach my $line (@lines)
    {
        #0:00    Asia Sagripanti - "Careless Whisper"  (Italy)
        # 0:00    Asia Sagripanti - "Careless Whisper"  (Italy)
        # if ($line =~ /^\s+(\d+:\d+)([^-]+)/)
        # if ($line =~ /^\s+(\d+:\d+)([^-]+)[^"]+"([^"]+)"[^(]+\(([^)]+)\)/)
        if ($line =~ /^\s+(\d+:\d+)([^-]+)-([^(]+)\(([^)]+)\)/)
        {
            my $time = $1;
            my $name = $2;
            my $song = $3;
            my $country = $4;
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $line =~ s/^\s+//;
            $line =~ s/\s+$//;
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $name =~ s/^\s+//;
            $name =~ s/\s+$//;
            $song =~ s/^\s+//;
            $song =~ s/\s+$//;
            $song =~ s/^"//;
            $song =~ s/"$//;
            $country =~ s/\s+$//;
            $country =~ s/^\s+//;
            $country =~ s/ 2018$//;
            $country =~ s/ 2017$//;
            $country =~ s/ 2016$//;
            $country =~ s/ 2015$//;
            $country =~ s/ 2014$//;
            $country =~ s/ 2013$//;
            $country =~ s/ 2012$//;
            print "$line\n";
            print "  $time\n";
            print "  $name\n";
            print "  $song\n";
            print "  $country\n";
            $names{$name}++;
            $songs{$song}++;
            $countries{$country}++;
        }
        # 3:30   Charlotte Cardin Goyer - You know I'm no good
        elsif ($line =~ /^\s+(\d+:\d+)([^-]+)-(.*)$/)
        {
            my $time = $1;
            my $name = $2;
            my $song = $3;
            my $country = "NOT POSTED";
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $line =~ s/^\s+//;
            $line =~ s/\s+$//;
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $name =~ s/^\s+//;
            $name =~ s/\s+$//;
            $song =~ s/^\s+//;
            $song =~ s/\s+$//;
            $song =~ s/^"//;
            $song =~ s/"$//;
            print "$line\n";
            print "  $time\n";
            print "  $name\n";
            print "  $song\n";
            print "  $country\n";
            $names{$name}++;
            $songs{$song}++;
            $countries{$country}++;
        }
        # 18:45   Inga Jankauskaitė, Donatas Montvydas, Justinas Jarutis, Leon Somov and Monika Marija "Adventure of a Lifetime" Lietuvos Balsas / The Voice Of Lithuania (bonus video)
        elsif ($line =~ /^\s+(\d+:\d+)([^"]+)"(.*)"[^\/]+\/(.*)$/)
        {
            my $time = $1;
            my $name = $2;
            my $song = $3;
            my $country = $4;
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $line =~ s/^\s+//;
            $line =~ s/\s+$//;
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $name =~ s/^\s+//;
            $name =~ s/\s+$//;
            $song =~ s/^\s+//;
            $song =~ s/\s+$//;
            $song =~ s/^"//;
            $song =~ s/"$//;
            $country =~ s/\s+$//;
            $country =~ s/^\s+//;
            $country =~ s/ 2018$//;
            $country =~ s/ 2017$//;
            $country =~ s/ 2016$//;
            $country =~ s/ 2015$//;
            $country =~ s/ 2014$//;
            $country =~ s/ 2013$//;
            $country =~ s/ 2012$//;
            print "$line\n";
            print "  $time\n";
            print "  $name\n";
            print "  $song\n";
            print "  $country\n";
            $names{$name}++;
            $songs{$song}++;
            $countries{$country}++;
        }
        elsif ($line =~ /^$/)
        {
            # print "EMPTY $line\n";
        }
        elsif ($line =~ /www.youtube.com/ || $line =~ /en.wikipedia.org/)
        {
            # print "URL $line\n";
        }
        elsif ($line =~ /INDEX OF MUSIC/)
        {
            # print "INDEX $line\n";
        }
        elsif ($line =~ /Today every ukrainian knows/ ||
            $line =~ /the Day of the Heavenly Hundred Heroes/ ||
            $line =~ /50 is currently not online/ ||
            $line =~ /XXX no triple X clip/ ||
            $line =~ /top 9 blind auditions/)
        {
            # print "MISC $line\n";
        }
        else
        {
            print "WHAT $line\n";
        }
    }
}

sub main
{
    count("top9.txt");
    stats();
}

main();
