#!/usr/bin/env bash
# Personal bash script for gather all of the subdomains used
cd /opt/bounty-targets-data/ && git pull
cat $1 /opt/bounty-targets-data/data/wildcards.txt | sed 's/^\*\.//g' | grep -vE '\*' | grep -v sys.comcast.net | sort -u
