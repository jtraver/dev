#!/usr/bin/env bash

SERVER_REPO=citrusleaf/aerospike-server
OLD_SERVER_BUILD_COUNT=21
NEW_SERVER_BUILD_COUNT=16
SERVER_BUILD_TIMEOUT=120
TOOLS_REPO=citrusleaf/aerospike-tools
TOOLS_BUILD_COUNT=8
TOOLS_BUILD_TIMEOUT=40
MAC_WAKEUP_TIMEOUT=150
MAC_BUILD_MACHINE=192.168.120.199

#buildfile /Users/jtraver/dev/git/citrusleaf/aerospike-server/.build.yml
#  centos-6 community
#  centos-7 community
#  debian-7 community
#  debian-8 community
#  ubuntu-12.04 community
#  ubuntu-14.04 community
#  ubuntu-16.04 community
#  centos-6 enterprise
#  centos-7 enterprise
#  debian-7 enterprise
#  debian-8 enterprise
#  ubuntu-12.04 enterprise
#  ubuntu-14.04 enterprise
#  ubuntu-16.04 enterprise
#
#buildfile /Users/jtraver/dev/git/citrusleaf/aerospike-tools/.build.yml
#  centos-6 default
#  centos-7 default
#  debian-7 default
#  debian-8 default
#  ubuntu-12.04 default
#  ubuntu-14.04 default
#  ubuntu-16.04 default
# TOOLS_COMPLETED=`$BUILDCTL ps --repo $TOOLS_REPO --ref $TOOLS_VERSION --all | grep Completed | wc -l`

main() {
    PROGNAME=$0
    # SERVER_VERSION=$1
    # SERVER_BRANCH=$2
    # TOOLS_VERSION=$3
    # TOOLS_BRANCH=$4
    echo OLD_SERVER_BUILD_COUNT $OLD_SERVER_BUILD_COUNT
    echo NEW_SERVER_BUILD_COUNT $NEW_SERVER_BUILD_COUNT
    echo TOOLS_BUILD_COUNT $TOOLS_BUILD_COUNT
    # ../publish/work/aerospike-server/source/.build.yml
    # ../tools/work/aerospike-tools/.build.yml
    NEW_SERVER_BUILD_COUNT=`build2.py ~jtraver/dev/git/citrusleaf/aerospike-server/.build.yml | wc -l`
    TOOLS_BUILD_COUNT=`build2.py ~jtraver/dev/git/citrusleaf/aerospike-tools/.build.yml | wc -l`
    echo OLD_SERVER_BUILD_COUNT $OLD_SERVER_BUILD_COUNT
    echo NEW_SERVER_BUILD_COUNT $NEW_SERVER_BUILD_COUNT
    echo TOOLS_BUILD_COUNT $TOOLS_BUILD_COUNT
}

main $@
