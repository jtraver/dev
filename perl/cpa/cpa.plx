#!/usr/bin/perl -w

use diagnostics;
use warnings;
use strict;

# file has a type and an extension

my %ftypes;     # file types
my %fexts;      # file extensions
my %files;      # all files
my %cfiles;
my %hfiles;
my %funcdef;        # function definition
my %funcdec;        # function declaration
my %funcparents;    # key is called by val
my %funcchildren;   # val is called by key
my %funcs;          # everything the faulty parser thought might be a function or macro: defined, declared or called
my %funcinfo;

# not vaguely working yet
sub show_parents
{
    my ($func1, $indent1) = @_;
    if ($indent1 <= 0)
    {
        print "  $func1\n";
        return
    }
    my $filler = sprintf("%.*s", $indent1 * 2, "                                                                                                                                                                 ");
    print "  $filler$func1\n";
    if (!defined($funcs{$func1}))
    {
        print "  $func1 is not listed in funcs hash\n";
        return;
    }
    if (defined($funcparents{$func1}))
    {
        my $parentsref = $funcparents{$func1};
        my %parentshash = %$parentsref;
        for my $parent (sort keys %parentshash)
        {
            show_parents($parent, $indent1 - 1);
        }
    }
}

sub main
{
    # print "main\n";
    find_files();
    check_c_files();
    check_header_files();
    if (0)
    {
        my $func1 = "fetch_bytes_from_file";
        my $indent1 = 10;
        print "\nshowing parents for $func1 to $indent1 levels, not checking for dupes\n";
        show_parents($func1, $indent1);
        exit 1;
    }
    list_functions();
    print "\n";
    # show_function("fetch_bytes_from_file");
    # show_function("cf_fetch_bytes");            # fetch_bytes_from_file
    # show_function('cf_fetch_string');               # cf_fetch_bytes
    # show_function('cf_fetch_validate_string');          # cf_fetch_string
    # show_function('as_dc_cfg_post_process');                # cf_fetch_validate_string
    # show_function('as_ldap_config_check');                  # cf_fetch_validate_string
    # show_function('set_config_dc');                         # cf_fetch_validate_string
    # show_function('cf_vault_cfg_post_process');         # cf_fetch_string
    # show_function('cfg_post_process');                      # cf_vault_cfg_post_process
    # show_function('create_login_request');              # cf_fetch_string
    # show_function('login_node');                            # create_login_request
    # show_function('serv_bind_query_user');              # cf_fetch_string
    # show_functin('serv_authenticate');                      # serv_bind_query_user
    # show_functin('serv_setup_query_user');                  # serv_bind_query_user
    # show_function('tls_read_password');                 # cf_fetch_string
    # show_function('as_config_post_process');                # tls_read_password
    # show_function('drv_init_encryption_key');       # cf_fetch_bytes
    # show_function('as_storage_cfg_init_pmem');          # drv_init_encryption_key
    # show_function('as_storage_cfg_init_ssd');           # drv_init_encryption_key
    # show_function('load_cert');                     # cf_fetch_bytes
    # show_function('create_context');                    # load_cert
    # show_function('reload_cert_and_key');               # load_cert
    # show_function('load_private_key');              # cf_fetch_bytes
    # show_function('create_context');                    # load_private_key    REPEAT
    # show_function('reload_cert_and_key');               # load_private_key    REPEAT
    show_function('aerospike_connect');
    show_function('as_policy_event_init');
    show_function('connect_to_server');
    show_function('example_connect_to_aerospike_with_udf_config');
    show_function('usage');
    parent 'as_create_event_loops'
    parent 'as_set_external_event_loop'
    parent 'create_event_loop_with_delay_queue'
  as_policy_event_init calls additional functions

looking for function connect_to_server
  connect_to_server has callers
    parent 'run_benchmark'
  connect_to_server calls additional functions

looking for function example_connect_to_aerospike_with_udf_config
  example_connect_to_aerospike_with_udf_config has callers
    parent 'DETAIL'
    parent 'example_connect_to_aerospike'
    parent 'main'
  example_connect_to_aerospike_with_udf_config calls additional functions

looking for function usage
  usage has callers
    parent 'example_get_opts'
    parent 'usage'

    show_function('as_lookup_node');
    show_function('as_cluster_seed_node');
    show_function('as_peers_duplicate');
    show_function('as_cluster_tend');
    show_function('as_cluster_tender');
    show_function('as_shm_tender');
    show_function('as_wait_till_stabilized');
    show_function('as_cluster_init');
    show_function('as_cluster_create');
    show_function('as_shm_create');
}

sub show_function
{
    my ($func1) = @_;
    print "\nlooking for function $func1\n";
    if (!defined($funcs{$func1}))
    {
        print "  $func1 is not listed in funcs hash\n";
        return;
    }
    if (defined($funcparents{$func1}))
    {
        print "  $func1 has callers\n";
        my $parentsref = $funcparents{$func1};
        my %parentshash = %$parentsref;
        for my $parent (sort keys %parentshash)
        {
            print "    parent '$parent'\n";
        }
    }
    if (defined($funcchildren{$func1}))
    {
        print "  $func1 calls additional functions\n";
    }
}

# "you can not make a parser from regex" :)
sub check_file
{
    my ($filename) = @_;
    my @lines1 = `cat $filename`;
    chomp(@lines1);
    my $lineno = 0;
    my $current_scope_function = "";
    for my $line1 (@lines1)
    {
        $lineno++;
        my $line0 = $line1;
        $line1 =~ s/^#define //;
        my @fields1 = split("\\(", $line1);
        my $ilast1 = @fields1 - 1;
        if ($ilast1 <= 0)
        {
            next;
        }
        my $fieldn = $fields1[$ilast1];
        my $func1 = "";
        for (my $i1 = 0; $i1 < $ilast1; $i1++)
        {
            my $field1 = $fields1[$i1];
            # print "  $i1 $field1\n";
            my @fields2 = split(" ", $field1);
            my $ilast2 = @fields2 - 1;
            if ($ilast2 < 0)
            {
                next;
            }
            $func1 = $fields2[$ilast2];
            $func1 =~ s/^\*+//;
            my $func0 = $func1;
            # print "  func1 is $func1 before trim\n";
            # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
            $func1 =~ s/^\s+//;
            $func1 =~ s/\s+$//;
            $func1 =~ s/^[^a-zA-Z0-9_]+//;
            $func1 =~ s/^[0-9_]+//;
            $func1 =~ s/[^a-zA-Z0-9_]+$//;
            # print "  func1 is $func1 after trim\n";
            if ($func1 ne $func0)
            {
                # print "  function $func0 WAS TRIMMED to $func1\n";
                next;
            }
            if ($func1 eq "while" ||
                $func1 eq "void")
            {
                next;
            }
            if ($func1 eq "")
            {
                next;
            }
            # print "  looks like a func to me: $func1\n";
            $funcs{$func1}++;
            $funcinfo{$func1}{$filename}{$lineno} = $line0;
            if ($current_scope_function ne "")
            {
                $funcchildren{$current_scope_function}{$func1} = $filename;
            }
        }
        if ($line1 =~ /^[a-zA-Z_][a-zA-Z0-9_]+\(/)
        {
            # print "  DEFINITION of '$func1' $filename $line1\n";
            if ($line1 =~ /^.*\)\s*;\s*$/)
            {
                $funcdec{$func1} = $filename;
                $current_scope_function = "";
            }
            else
            {
                $funcdef{$func1} = $filename;
                $current_scope_function = $func1;
            }
        }
        else
        {
            if ($current_scope_function ne "")
            {
                $funcparents{$func1}{$current_scope_function} = $filename;
            }
        }
    }
    # exit 1;
}

# "you can not make a parser from regex" :)
sub check_c_files
{
    # print "check_c_files\n";
    my @cfiles = sort keys %cfiles;
    my $ctotal = @cfiles;
    my $ccount = 0;
    for my $cfile (@cfiles)
    {
        $ccount++;
        # print "$ccount of $ctotal $cfile\n";
        check_file($cfile);
    }
}

# "you can not make a parser from regex" :)
sub check_header_files
{
    my @hfiles = sort keys %hfiles;
    my $htotal = @hfiles;
    my $hcount = 0;
    for my $hfile (@hfiles)
    {
        $hcount++;
        # print "$hcount of $htotal $hfile\n";
        check_file($hfile);
    }
}

sub old_check_header_files
{
    my $hfile = "";
    {
        my @lines1 = `cat $hfile`;
        chomp(@lines1);
        my $lineno = 0;
        for my $line1 (@lines1)
        {
            $lineno++;
            if ($line1 =~ /__attribute__/ && $line1 =~ /__packed__/)
            {
                next;
            }
            if ($line1 eq " * Copyright (C) 2017-2020 Aerospike, Inc." ||
                $line1 eq " * Copyright (C) 2008-2020 Aerospike, Inc.")
            {
                next;
            }
            $line1 =~ s/^#define //;
            my @fields1 = split("\\(", $line1);
            my $ilast1 = @fields1 - 1;
            if ($ilast1 <= 0)
            {
                next;
            }
            # print "$hfile $line1\n";
            # print "  $ilast1\n";
            my $fieldn = $fields1[$ilast1];
            #if ($fieldn eq $line1)
            #{
            #    next;
            #}
            for (my $i1 = 0; $i1 < $ilast1; $i1++)
            {
                my $field1 = $fields1[$i1];
                # print "  $i1 $field1\n";
                my @fields2 = split(" ", $field1);
                my $ilast2 = @fields2 - 1;
                if ($ilast2 < 0)
                {
                    # print "WHAT $hfile $line1 $field1\n";
                    # exit 4;
                    next;
                }
                my $func1 = $fields2[$ilast2];
                $func1 =~ s/^\*+//;
                my $func0 = $func1;
                # print "  func1 is $func1 before trim\n";
                # trim $line =~ s/^\s+//; $line =~ s/\s+$//;
                $func1 =~ s/^\s+//;
                $func1 =~ s/\s+$//;
                $func1 =~ s/^[0-9_]+//;
                $func1 =~ s/^[^a-zA-Z0-9_]+//;
                $func1 =~ s/[^a-zA-Z0-9_]+$//;
                # print "  func1 is $func1 after trim\n";
                if ($func1 ne $func0)
                {
                    # print "  function $func0 WAS TRIMMED to $func1\n";
                    next;
                }
                if ($func1 eq "while" ||
                    $func1 eq "void")
                {
                    next;
                }
                if ($func1 eq "")
                {
                    next;
                }
                # print "  looks like a func to me: $func1\n";
                $funcs{$func1}++;
                $funcdec{$func1} = $hfile;
                $funcinfo{$func1}{$hfile}{$lineno} = $line1;
            }
        }
        # exit 1;
    }
}

sub find_files
{
    # print "find_files\n";
    my @find1 = `find ..`;
    chomp(@find1);
    my $ftotal = @find1;
    my $fcount = 0;
    for my $file1 (@find1)
    {
        # 1 FAIL ../.git/packed-refs with extension packed-refs has type FILE TYPE UNKNOWN
        $fcount++;
        # print "$fcount of $ftotal file1 $file1\n";
        if ($file1 =~ /\.\.\/\.git\//)
        {
            # print "$file1 is down .git: skip it\n";
            next;
        }
        # ../SFGREP
        if ($file1 =~ /\.\.\/SFGREP\//)
        {
            # print "$file1 is down .git: skip it\n";
            next;
        }
        my $type1 = "FILE TYPE UNKNOWN";
        my $ext1 = "NO FILE EXTENSION";
        my @path1 = split("/", $file1);
        my $plast = @path1 - 1;
        my $repodir = "";
        my $lastdir = "";
        if (-d $file1)
        {
            # print "$file1 is a directory\n";
            $lastdir = $path1[$plast];
            # print "  $lastdir is a directory\n";
        }
        if ($plast >= 1)
        {
            $repodir = $path1[1];
        }
        my $topleveldir = "";
        if ($plast >= 2)
        {
            $topleveldir = $path1[2];
        }
        if ($repodir eq "CPA")
        {
            # print "  found CPA dir\n";
            next;
        }
        if ($topleveldir eq ".git" || $lastdir eq ".git")
        {
            # print "  found .git dir\n";
            next;
        }
        if (-d $file1)
        {
            $type1 = "directory";
        }
        else
        {
            # print "  topleveldir = $topleveldir\n";
            my $basename1 = $path1[$plast];
            # print "  basename = $basename1\n";
            my @fields1 = split("\\.", $basename1);
            my $last1 = @fields1 - 1;
            $ext1 = $fields1[$last1];
            # print "  ext = $ext1\n";
            if ($ext1 eq "sh" || $ext1 eq "bash" || $ext1 eq "tcsh" ||  
                $ext1 eq "clang-format" ||
                $ext1 eq "clang-format-check" ||
                $ext1 eq "nostrip" ||
                $ext1 eq "prepare_xcode" ||
                $ext1 eq "normal" ||
                $ext1 eq "strip" ||
                $ext1 eq "check-exports" ||
                $ext1 eq "error" ||
                $ext1 eq "run" ||
                $ext1 eq "env" ||
                $ext1 eq "output" ||
                $ext1 eq "input" ||
                $ext1 eq "run-suites" ||
                $ext1 eq "install-sh" ||
                $ext1 eq "INSTALL" ||
                $ext1 eq "asd-systemd-helper" ||
                $ext1 eq "init-script" ||
                $ext1 eq "server" ||
                $ext1 eq "aerospike-destroy" ||
                $ext1 eq "aerospike-stop" ||
                $ext1 eq "aerospike-status" ||
                $ext1 eq "aerospike-start" ||
                $ext1 eq "asparsemem" ||
                $ext1 eq "query_annotate" ||
                $ext1 eq "stp" ||
                $ext1 eq "iddecode" ||
                $ext1 eq "package_src" ||
                $ext1 eq "set_version" ||
                $ext1 eq "package_type" ||
                $ext1 eq "client" ||
                $ext1 eq "install" ||
                $ext1 eq "platform" ||
                $ext1 eq "package" ||
                $ext1 eq "asd-coldstart" ||
                $ext1 eq "aerospike-restart" ||
                $ext1 eq "aerospike-init" ||
                $ext1 eq "aerospike" ||
                $ext1 eq "deb" ||
                $ext1 eq "init-telemetry-script" ||
                $ext1 eq "os_version" ||
                $ext1 eq "logrotate_asd" ||
                $ext1 eq "logrotate_telemetry" ||
                $ext1 eq "asinstall" ||
                $ext1 eq "version" || $ext1 eq "gen_version" || $ext1 eq "prep-ce")
            {
                $type1 = "shell script";
            }
            elsif ($ext1 eq "yml" || $ext1 eq "yaml")
            {
                $type1 = "YAML";
            }
            elsif ($ext1 eq "plx")
            {
                $type1 = "perl script";
            }
            elsif ($ext1 eq "log")
            {
                $type1 = "log file";
            }
            elsif ($ext1 eq "git")
            {
                $type1 = "dot git locater";
            }
            elsif ($ext1 eq "supp")
            {
                $type1 = "valgrind suppression file";
            }
            elsif ($ext1 eq "png" ||
                $ext1 eq "jpg")
            {
                $type1 = "media";
            }
            elsif ($ext1 eq "man")
            {
                $type1 = "man page";
            }
            elsif ($ext1 eq "1" ||
                $ext1 eq "lua" ||
                $ext1 eq "info" ||
                $ext1 eq "def" ||
                $ext1 eq "bat" ||
                $ext1 eq "orig" ||
                $ext1 eq "rc" ||
                $ext1 eq "dasc" ||
                $ext1 eq "COPYRIGHT" ||
                $ext1 eq "pc" ||
                $ext1 eq "ico")
            {
                $type1 = "Lua source file";
            }
            elsif ($ext1 eq "py")
            {
                $type1 = "Python source file";
            }
            elsif ($ext1 eq "c" ||
                $ext1 eq "cpp" ||
                $ext1 eq "cc")
            {
                $type1 = "C source file";
            }
            elsif ($ext1 eq "h" ||
                $ext1 eq "hpp")
            {
                $type1 = "C header file";
            }
            elsif ($ext1 eq "css" ||
                $ext1 eq "rst" ||
                $ext1 eq "ChangeLog" ||
                $ext1 eq "CHANGES" ||
                $ext1 eq "html" ||
                $ext1 eq "xsl" ||
                $ext1 eq "xml")
            {
                $type1 = "documentation";
            }
            elsif ($ext1 eq "vars" ||
                $ext1 eq "am" ||
                # FAIL ../install_libevent with extension install_libevent has type FILE TYPE UNKNOWN
                $ext1 eq "install_libev" ||
                $ext1 eq "install_libuv" ||
                $ext1 eq "install_libevent" ||
                $ext1 eq "cmake" ||
                $ext1 eq "dep" ||
                $ext1 eq "targets" ||
                $ext1 eq "txt" ||
                $ext1 eq "mk" ||
                $ext1 eq "in" || $ext1 eq "Makefile")
            {
                $type1 = "makefile";
            }
            elsif ($ext1 eq "conf" ||
                $ext1 eq "nuspec" ||
                $ext1 eq "spec" ||
                $ext1 eq "xcscmblueprint" ||
                $ext1 eq "swig" ||
                $ext1 eq "cfg" ||
                $ext1 eq "ac" ||
                $ext1 eq "guess" ||
                $ext1 eq "sub" ||
                $ext1 eq "sln" ||
                $ext1 eq "props" ||
                $ext1 eq "vcxproj" ||
                $ext1 eq "config" ||
                $ext1 eq "filters" ||
                $ext1 eq "xcworkspacedata" ||
                $ext1 eq "pbxproj" ||
                $ext1 eq "sysconfig" ||
                $ext1 eq "d" ||
                $ext1 eq "coldstart" ||
                $ext1 eq "default" ||
                $ext1 eq "service" ||
                $ext1 eq "head" ||
                $ext1 eq "tail" ||
                $ext1 eq "tmpfiles" ||
                $ext1 eq "server-64" ||
                $ext1 eq "conffiles" ||
                $ext1 eq "telemetry" ||
                $ext1 eq "xdr-files" ||
                $ext1 eq "server-spec-telemetry-systemd" ||
                $ext1 eq "server-spec-telemetry" ||
                $ext1 eq "server-spec-base" ||
                $ext1 eq "server-spec-telemetry-sysv" ||
                $ext1 eq "server-spec-sysv" ||
                $ext1 eq "as-files" || $ext1 eq "doxyfile" || $ext1 eq "server-spec-scripts-systemd" || $ext1 eq "server-spec-logrotate" || $ext1 eq "server-spec-config" || $ext1 eq "server-spec-scripts" || $ext1 eq "server-spec-systemd" || $ext1 eq "server-spec-files")
            {
                $type1 = "configuration file";
            }
            elsif ($ext1 eq "LICENSE" ||
                $ext1 eq "COPYING" ||
                $ext1 eq "LICENSE-APACHE" ||
                $ext1 eq "copyright" ||
                $ext1 eq "submodule-licenses" ||
                $ext1 eq "EE" || $ext1 eq "LICENSE-AGPL" || $ext1 eq "CE" || $ext1 eq "3rdParty")
            {
                $type1 = "license";
            }
            elsif ($ext1 eq "gitmodules" ||
                $ext1 eq "gitattributes" ||
                $ext1 eq "gitignore")
            {
                $type1 = "git helper";
            }
            elsif ($ext1 eq "md" || $ext1 eq "README")
            {
                $type1 = "Mark Down";
            }
        }
        if ($type1 eq "directory")
        {
            # print "  'type $type1' 'dir $file1'\n";
        }
        else
        {
            # print "  'type $type1' 'ext $ext1' 'file $file1'\n";
            $files{$file1}{'EXT'} = $ext1;
            $files{$file1}{'TYPE'} = $type1;
            $ftypes{$type1}{$file1}++;
            $fexts{$ext1}{$file1}++;
            if ($type1 eq "C source file")
            {
                $cfiles{$file1} = $ext1;
            }
            elsif ($type1 eq "C header file")
            {
                $hfiles{$file1} = $ext1;
            }
            if ($type1 eq "FILE TYPE UNKNOWN")
            {
                # FAIL ../install_libevent with extension install_libevent has type FILE TYPE UNKNOWN
                print "1 FAIL $file1 with extension $ext1 has type $type1\n";
                exit 2;
            }
            if ($ext1 eq "NO FILE EXTENSION")
            {
                print "2 FAIL $file1 extension is $ext1\n";
                exit 3;
            }
        }
    }
}

sub list_functions
{
    print "\nfunction list\n";
    my @funcs = sort keys %funcs;
    my $ftotal = @funcs;
    my $fcount = 0;
    for my $func (@funcs)
    {
        $fcount++;
        my $refcount = $funcs{$func};
        print "FUNC $fcount of $ftotal $func referenced $refcount times\n";
        print "  $func\n";
        if (defined($funcdef{$func}))
        {
            my $deffile = $funcdef{$func};
            print "  $func defined in file $deffile\n";
        }
        else
        {
            print "WARN found no definition for function $func\n";
        }
        if (!defined($funcparents{$func}))
        {
            print "3 FAIL found no caller for function $func\n";
        }
        my $fifileref = $funcinfo{$func};
        my %fifilehash = %$fifileref;
        for my $file (sort keys %fifilehash)
        {
            my $filinenoref = $fifilehash{$file};
            my %filinenohash = %$filinenoref;
            for my $lineno (sort keys %filinenohash)
            {
                my $line = $filinenohash{$lineno};
                print "  $file $lineno $line\n";
            }
        }
    }
}

main();
print STDERR "\n";
print "\n";
