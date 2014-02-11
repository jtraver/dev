#!/usr/bin/perl -w
use diagnostics;
use warnings;
use strict;
use File::Find;
$| = 1;
my $status = 800;
#my $status = 330;
#my $status = 800;
my $count = 0;
sub wanted
{
        # print "$_\n";
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
                print OUTPUT "$name\n";
        }
}
my $output = "TextFiles.txt";
open(OUTPUT, ">$output") or die "Can't write $output: $!";
File::Find::find(\&wanted, "..");
close(OUTPUT);
print "\n";
