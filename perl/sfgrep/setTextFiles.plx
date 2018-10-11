#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

use File::Find;

$| = 1;
my $status = 800;
my $count = 0;

sub wanted
{
        $count++;
        if ($count % $status == 0)
        {
                print ".";
        }
        my $name = $File::Find::name;
        if ($name =~ /\.\.\/jtraver\//)
        {
            print "skipping $name\n";
        }
        elsif (! -d && -T &&
                $name !~ /\/centos\/status\/runs\// &&
                $name !~ /\/centos\/status\/\.17/ &&
                $name !~ /\.css\.map$/ &&
                $name !~ /\.min\.css$/ &&
                $name !~ /\.min\.js$/ &&
                $name !~ /\/SFGREP\// &&
                $name !~ /\/old.SFGREP\// &&
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
