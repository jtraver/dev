#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

my $status = 0;
my @files;
my $count = 0;
$| = 1;
my $word = "public";
if (!defined($word) || $word eq "")
{
        die "need a word to search for";
}
mkdir "CPAJAVA";
my $output = "CPAJAVA/$word.txt";
if (-e $output && 0)
{
}
else
{
        open(OUTPUT, ">$output") or die "Can't write $output: $!";
        load_files();
        my $save_rs = $/;
        foreach my $file (sort @files)
        {
        if ($file !~ /\.java$/)
        {
            next;
        }
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
                                print OUTPUT "---------------------------------------------------------------------------\n";
                                print OUTPUT "---------------------------------------------------------------------------\n";
                                print OUTPUT "| $file\n";
                                print OUTPUT "---------------------------------------------------------------------------\n";
                                $/ = $save_rs;
                                $file_open = open(FILE, $file);
                                if ($file_open)
                                {
                                        my @lines = <FILE>;
                                        close(FILE);
                                        chomp(@lines);
										my $need_signature = 0;
										my $signature = "";
                                        foreach $line (@lines)
                                        {
                                                if ($line =~ /$word/i)
                                                {
                                                        print OUTPUT "\t$line\n";
														if ($line =~ /\(/)
														{
															$need_signature = 1;
															print OUTPUT "\tthis line looks like a function: '$line'\n";
															if ($line =~ /\{/)
															{
																print OUTPUT "\tthis line looks ok: '$line'\n";
																print OUTPUT "SIGNATURE '$line'\n";
																$need_signature = 0;
																$signature = "";
															}
															else
															{
																if ($line =~ /;/)
																{
																	print OUTPUT "\tthis line is probably not a function: '$line'\n";
																}
																else
																{
																	print OUTPUT "\tthis line does NOT look OK: '$line'\n";
																	$signature = $line;
																}
															}
														}
                                                }
												elsif ($need_signature == 1)
												{
                                                        print OUTPUT "\tlooking for end of signature in '$line'\n";
														if ($line =~ /\{/)
														{
																print OUTPUT "\tthis line looks like end of signature: '$line'\n";
																$signature .= " $line";
																print OUTPUT "SIGNATURE '$signature'\n";
																$need_signature = 0;
																$signature = "";
														}
														else
														{
															if ($line =~ /;/)
															{
																print OUTPUT "\tthis continuation line is probably not a function: '$line'\n";
																print OUTPUT "\tdropping start of this signature: '$signature'\n";
																$need_signature = 0;
																$signature = "";
															}
															else
															{
																print OUTPUT "\tthis line does NOT look OK: '$line'\n";
																$signature .= " $line";
															}
														}
												}
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
        close(OUTPUT);
        print "\n";
}
my $cmd = "vi \"$output\" find_java_signatures.plx";
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
}
