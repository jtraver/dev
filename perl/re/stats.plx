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
    my $max = 0;
    my $maxname;
    for my $name (sort keys %names)
    {
        my $count = $names{$name};
        if ($count > $max)
        {
            $max = $count;
            $maxname = $name;
        }
        if ($count > 1)
        {
            print "$name $count\n";
        }
    }
    for my $name (sort keys %names)
    {
        my $count = $names{$name};
        if ($count == 1)
        {
            print "$name $count\n";
        }
    }
    print "max name $maxname $max\n";
    print "\n";
    print "Songs\n";
    $max = 0;
    my $maxsong;
    for my $song (sort keys %songs)
    {
        my $count = $songs{$song};
        if ($count > $max)
        {
            $max = $count;
            $maxsong = $song;
        }
        if ($count > 2)
        {
            print "$song $count\n";
        }
    }
    for my $song (sort keys %songs)
    {
        my $count = $songs{$song};
        if ($count == 2)
        {
            print "$song $count\n";
        }
    }
    for my $song (sort keys %songs)
    {
        my $count = $songs{$song};
        if ($count == 1)
        {
            print "$song $count\n";
        }
    }
    print "max song $maxsong $max\n";
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
        elsif ($line =~ /^\s+(\d+:\d+)([^"]+)"(.*)"[^\/]+(.*)$/)
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
