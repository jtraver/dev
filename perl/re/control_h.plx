#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# remove backspace bold technique characters from a man page
sub main
{
    fix_man("ps.man");
}

sub fix_man
{
    my ($filename) = @_;
    my $fileopen = open(MAN, $filename);
    if (!$fileopen)
    {
        print STDERR "ERROR: could not read $filename: $!";
        print STDERR "\n";
        return;
    }
    my @lines = <MAN>;
    close(MAN);
    chomp(@lines);
    foreach my $line (@lines)
    {
        $line =~ s/.//g;
        print "$line\n";
    }
}

main();

#
#Johns-MacBook-Pro-3:env jtraver$ ps --help
#ps: illegal option -- -
#usage: ps [-AaCcEefhjlMmrSTvwXx] [-O fmt | -o fmt] [-G gid[,gid...]]
#          [-g grp[,grp...]] [-u [uid,uid...]]
#          [-p pid[,pid...]] [-t tty[,tty...]] [-U user[,user...]]
#       ps [-L]
#
#
#Johns-MacBook-Pro-3:ps jtraver$ ps -L
#%cpu %mem acflag acflg args blocked caught comm command cpu cputime etime f flags gid group ignored inblk inblock jobc ktrace ktracep lim login logname lstart majflt minflt msgrcv msgsnd ni nice nivcsw nsignals nsigs nswap nvcsw nwchan oublk oublock p_ru paddr pagein pcpu pending pgid pid pmem ppid pri pstime putime re rgid rgroup rss ruid ruser sess sig
#sigmask sl start stat state stime svgid svuid tdev time tpgid tsess tsiz tt tty ucomm uid upr user usrpri utime vsize vsz wchan wq wqb wql wqr xstat
#
