#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my @files;
my $status = 1;

sub main
{
    my $count = 0;

    my $line_limit = 2000;

    $| = 1;
    # my $word = shift;
    my $word = "cf_info";
    if (!defined($word) || $word eq "")
    {
            die "need a word to search for";
    }
    mkdir "REGEX";
    my $output = "REGEX/$word.txt";

    my %contexts;
    $contexts{"cont"} = "context passed as variable";
    $contexts{"CF_MISC"} = "misc";
    $contexts{"CF_ALLOC"} = "alloc";
    $contexts{"CF_ARENAX"} = "arenax";
    $contexts{"CF_HARDWARE"} = "hardware";
    $contexts{"CF_JEM"} = "jem";
    $contexts{"CF_MSG"} = "msg";
    $contexts{"CF_RBUFFER"} = "rbuffer";
    $contexts{"CF_SOCKET"} = "socket";
    $contexts{"CF_TLS"} = "tls";
    $contexts{"AS_AGGR"} = "aggr";
    $contexts{"AS_AS"} = "as";
    $contexts{"AS_BATCH"} = "batch";
    $contexts{"AS_BIN"} = "bin";
    $contexts{"AS_CFG"} = "config";
    $contexts{"AS_CLUSTERING"} = "clustering";
    $contexts{"AS_COMPRESSION"} = "compression";
    $contexts{"AS_DEMARSHAL"} = "demarshal";
    $contexts{"AS_DRV_SSD"} = "drv_ssd";
    $contexts{"AS_EXCHANGE"} = "exchange";
    $contexts{"AS_FABRIC"} = "fabric";
    $contexts{"AS_GEO"} = "geo";
    $contexts{"AS_HB"} = "hb";
    $contexts{"AS_HLC"} = "hlc";
    $contexts{"AS_INDEX"} = "index";
    $contexts{"AS_INFO"} = "info";
    $contexts{"AS_INFO_PORT"} = "info-port";
    $contexts{"AS_JOB"} = "job";
    $contexts{"AS_LDT"} = "ldt";
    $contexts{"AS_MIGRATE"} = "migrate";
    $contexts{"AS_MON"} = "mon";
    $contexts{"AS_NAMESPACE"} = "namespaces";
    $contexts{"AS_NSUP"} = "nsup";
    $contexts{"AS_PARTICLE"} = "particle";
    $contexts{"AS_PARTITION"} = "partition";
    $contexts{"AS_PAXOS"} = "paxos";
    $contexts{"AS_PREDEXP"} = "predexp";
    $contexts{"AS_PROTO"} = "proto";
    $contexts{"AS_PROXY"} = "proxy";
    $contexts{"AS_QUERY"} = "query";
    $contexts{"AS_RECORD"} = "record";
    $contexts{"AS_RW"} = "rw";
    $contexts{"AS_SCAN"} = "scan";
    $contexts{"AS_SECURITY"} = "security";
    $contexts{"AS_SINDEX"} = "sindex";
    $contexts{"AS_SMD"} = "smd";
    $contexts{"AS_STORAGE"} = "storage";
    $contexts{"AS_TRUNCATE"} = "truncate";
    $contexts{"AS_TSVC"} = "tsvc";
    $contexts{"AS_UDF"} = "udf";
    $contexts{"AS_XDR"} = "xdr";
    $contexts{"CF_FAULT_CONTEXT_UNDEF"} = "UNDEFINED CONTEXT";


    #if (-e $output)
    #{
    #}
    #else
    {
        open(OUTPUT, ">$output") or die "Can't write $output: $!";
        load_files();
        my $save_rs = $/;
        my $skipped_lines = 0;
        my $skipped_files = 0;
        my %regexes;
        my %cregexes;
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
                if ($line =~ /$word/)
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
                        # foreach $line (@lines)
                        for (my $i1 = 0; $i1 < @lines; $i1++)
                        {
                            my $line = $lines[$i1];
                            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
                            $line =~ s/^\s+//;
                            $line =~ s/\s+$//;
                            if ($line =~ /^#define/)
                            {
                                # print "skipping $line\n";
                                next;
                            }
                            if ($line =~ /^\*/)
                            {
                                # print "skipping $line\n";
                                next;
                            }
                            #if ($line =~ /define/)
                            #{
                            #    print "WHAT IS THIS define: $file\n";
                            #    print "WHAT IS THIS define: $line\n";
                            #}
                            my $len1 = length($line);
                            if ($len1 > $line_limit)
                            {
                                # print STDERR "line length is $len1 for $file\n";
                                $skipped++;
                                next;
                            }
                            if ($line =~ /$word/)
                            {
                                print OUTPUT "\tWORD $word -> $line\n";
                                my $msg = $line;
                                if ($msg =~ /;/)
                                {
                                    print OUTPUT "\t\tMSG -> $line\n";
                                }
                                else
                                {
                                    # print OUTPUT "\t\tMISSING -> $line\n";
                                    my $mcount = 0;
                                    my $i2 = $i1;
                                    while ($msg !~ /;/ && $mcount < 14)
                                    {
                                        $mcount++;
                                        $i2++;
                                        my $line2 = $lines[$i2];
                                        $line2 =~ s/^\s+//;
                                        $line2 =~ s/\s+$//;
                                        if (defined($line2))
                                        {
                                            # print "LINE2 $line2\n";
                                            $msg .= " $line2";
                                            # print "MSG $msg\n";
                                        }
                                        else
                                        {
                                            last;
                                        }
                                    }
                                    if ($msg =~ /;/)
                                    {
                                        print OUTPUT "\t\tMSG -> $msg\n";
                                    }
                                    else
                                    {
                                        print "WHAT IS THIS FILE: $file\n";
                                        print "WHAT IS THIS LINE: $line\n";
                                        print "WHAT IS THIS MESG: $msg\n";
                                        exit(1);
                                        next;
                                    }
                                }
                                if ($msg =~ /^\/\//)
                                {
                                    next;
                                }
                                if ($msg !~ /"/)
                                {
                                    # print "skipping $file $msg\n";
                                    next;
                                }
                                #my @fields1 = split("\"", $msg);
                                #my $regex1 = $fields1[1];
                                #if (defined($regex1))
                                #{
                                #    my $fi1 = 1;
                                #    while ($regex1 =~ /\\$/)
                                #    {
                                #        $fi1++;
                                #        my $field1 = $fields1[$fi1];
                                #        $regex1 .= '"' . $field1 . '"';
                                #        # print "file $file\n";
                                #        # print "line $line\n";
                                #        # print "mesg $msg\n";
                                #        # print "\t\tREGEX1 -> $regex1\n";
                                #        # exit(1);
                                #    }
                                #    # print "file $file\n";
                                #    # print "line $line\n";
                                #    # print "mesg $msg\n";
                                #    # print "\t\tREGEX1 -> $regex1\n";
                                #    print OUTPUT "\t\tREGEX1 -> $regex1\n";
                                #}
                                #else
                                #{
                                #    print "WHAT IS THIS FILE: $file\n";
                                #    print "WHAT IS THIS LINE: $line\n";
                                #    print "WHAT IS THIS MESG: $msg\n";
                                #    print "WHAT IS THIS REGX: $regex1\n";
                                #    exit(1);
                                #    next;
                                #}
                                my @fields2 = split(",", $msg);
                                my $context1 = $fields2[0];
                                my $regex1 = $fields2[1];
                                $context1 =~ s/cf_info\(//;
                                $context1 =~ s/cf_info_digest\(//;
                                $context1 =~ s/cf_info_binary\(//;
                                $context1 =~ s/^\s+//;
                                $context1 =~ s/\s+$//;
                                print OUTPUT "\t\tCONTEXT1 -> $context1\n";
                                my $context2 = $contexts{$context1};
                                if (defined($context2))
                                {
                                    print OUTPUT "\t\tCONTEXT2 -> $context2\n";
                                }
                                else
                                {
                                    print "WHAT IS THIS FILE: $file\n";
                                    print "WHAT IS THIS LINE: $line\n";
                                    print "WHAT IS THIS MESG: $msg\n";
                                    print "WHAT IS THIS REGX: $regex1\n";
                                    print "WHAT IS THIS CTX1: $context1\n";
                                    exit(1);
                                    next;
                                }
            # REGEX1 -> privsep to %d %d
                                my $regex2 = $regex1;
                                # $regex2 =~ s/%d/(\\d+)/g;
                                $regex2 =~ s/%d/(\\s+)/g;
                                if ($regex2 ne $regex1)
                                {
                                    print OUTPUT "\t\tREGEX2 -> $regex2\n";
                                    # print "\t\tREGEX2 -> $regex2\n";
                                }
            # REGEX1 -> <><><><><><><><><><>  %s build %s  <><><><><><><><><><>
                                my $regex3 = $regex2;
                                $regex3 =~ s/%c/(\\s+)/g;
                                $regex3 =~ s/%02u/(\\s+)/g;
                                $regex3 =~ s/%"PRId64"/(\\s+)/g;
                                $regex3 =~ s/%"PRIu64"/(\\s+)/g;
                                $regex3 =~ s/%"PRIu64/(\\s+)/g;
                                $regex3 =~ s/%" PRIu32 "/(\\s+)/g;
                                $regex3 =~ s/%" PRIu32/(\\s+)/g;
                                $regex3 =~ s/%016lX/(\\s+)/g;
                                $regex3 =~ s/%016lx/(\\s+)/g;
                                $regex3 =~ s/%.2lf/(\\s+)/g;
                                $regex3 =~ s/%.2f/(\\s+)/g;
                                $regex3 =~ s/%hu/(\\s+)/g;
                                $regex3 =~ s/%4d/(\\s+)/g;
                                $regex3 =~ s/%s/(\\s+)/g;
                                $regex3 =~ s/%u/(\\s+)/g;
                                $regex3 =~ s/%p/(\\s+)/g;
                                $regex3 =~ s/%lu/(\\s+)/g;
                                $regex3 =~ s/%lx/(\\s+)/g;
                                $regex3 =~ s/%ld/(\\s+)/g;
                                if ($regex3 ne $regex1)
                                {
                                    # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
                                    $regex3 =~ s/^\s+//;
                                    $regex3 =~ s/\s+$//;
                                    if ($regex3 =~ /^"/)
                                    {
                                        $regex3 =~ s/^"/\//;
                                    }
                                    else
                                    {
                                        $regex3 = "/$regex3";
                                    }
                                    if ($regex3 =~ /"$/)
                                    {
                                        $regex3 =~ s/"$/\//;
                                    }
                                    else
                                    {
                                        $regex3 = "$regex3/";
                                    }
                                    print OUTPUT "\t\tREGEX3 -> $regex3\n";
                                    # print "\t\tREGEX3 -> $regex3\n";
                                    $regexes{$regex3} = $context2;
                                    for (my $i1 = 2; $i1 < @fields2; $i1++)
                                    {
                                        my $field2 = $fields2[$i1];
                                        # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
                                        $field2 =~ s/^\s+//;
                                        $field2 =~ s/\s+$//;
                                        my $i2 = $i1 - 2;
                                        $cregexes{$context2}{$regex3}[$i2] = $field2;
                                    }
                                }
                                if ($regex3 =~ /%/ && $regex3 !~ /%%/)
                                {
                                    print "WHAT IS THIS FILE: $file\n";
                                    print "WHAT IS THIS LINE: $line\n";
                                    print "WHAT IS THIS MESG: $msg\n";
                                    print "WHAT IS THIS REGX: $regex3\n";
                                    print "WHAT IS THIS CTX1: $context1\n";
                                    exit(1);
                                }
                                #if ($regex3 =~ /"/)
                                #{
                                #    print "WHAT IS THIS FILE: $file\n";
                                #    print "WHAT IS THIS LINE: $line\n";
                                #    print "WHAT IS THIS MESG: $msg\n";
                                #    print "WHAT IS THIS REGX: $regex3\n";
                                #    print "WHAT IS THIS CTX1: $context1\n";
                                #    exit(1);
                                #}
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
        print OUTPUT "\n";
        print OUTPUT "regexes\n";
        my %rcontexts;
        foreach my $regex (sort keys %regexes)
        {
            my $context = $regexes{$regex};
            $rcontexts{$context}{$regex}++;
            print OUTPUT "$context $regex\n";
            # print "$context $regex\n";
        }
        print OUTPUT "\n";
        print OUTPUT "regex contexts\n";
        foreach my $context (sort keys %rcontexts)
        {
            print OUTPUT "$context\n";
            my $ref1 = $rcontexts{$context};
            my %hash1 = %$ref1;
            foreach my $regex (sort keys %hash1)
            {
                print OUTPUT "  $regex\n";
            }
        }
        print OUTPUT "\n";
        print OUTPUT "regex params\n";
        my $first1 = 0;
        my $what = 100000;
        foreach my $context (sort keys %cregexes)
        {
            if ($first1 == 0)
            {
                $first1 = 1;
                print OUTPUT "if (\$sub eq \"($context):\")\n";
            }
            else
            {
                print OUTPUT "elsif (\$sub eq \"($context):\")\n";
            }
            print OUTPUT "{\n";
            my $ref1 = $cregexes{$context};
            my %hash1 = %$ref1;
            my $first2 = 0;
            foreach my $regex (sort keys %hash1)
            {
                if ($first2 == 0)
                {
                    $first2 = 1;
                    print OUTPUT "    if (\$line =~ $regex)\n";
                }
                else
                {
                    print OUTPUT "    elsif (\$line =~ $regex)\n";
                }
                print OUTPUT "    {\n";
                my $ref2 = $hash1{$regex};
                my @arr2 = @$ref2;
                for (my $i2 = 0; $i2 < @arr2; $i2++)
                {
                    my $p2 = $arr2[$i2];
                    $p2 =~ tr/a-zA-Z0-9/_/cs;
                    my $i3 = $i2 + 1;
                    print OUTPUT "        my \$$p2 = \$$i3;\n";
                }
                for (my $i2 = 0; $i2 < @arr2; $i2++)
                {
                    my $p2 = $arr2[$i2];
                    $p2 =~ tr/a-zA-Z0-9/_/cs;
                    print OUTPUT "        update_stats(\"\$sub\" . \"_$p2\", \$$p2);\n";
                }
                print OUTPUT "    }\n";
            }
            print OUTPUT "    else\n";
            print OUTPUT "    {\n";
            $what++;
            print OUTPUT "        print \"WHAT $what line is this: \$sub in \$line\\n\";\n";
            print OUTPUT "    }\n";
            print OUTPUT "}\n";
        }
        print OUTPUT "else\n";
        print OUTPUT "{\n";
        $what++;
        print OUTPUT "    print \"WHAT $what sub is this: \$sub in \$line\\n\";\n";
        print OUTPUT "}\n";
        close(OUTPUT);
        print "\n";
    }
    my $cmd = "vi \"$output\"";
    system($cmd);
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

main();
