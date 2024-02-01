#!/usr/bin/env bash
# Usage: ./1-world_wide_web <domain> <subdomain>
# Display information about subdomains.

domain_information () {
    line=$(dig "$2"."$1" | grep -A1 'ANSWER SECTION:' | tr '\t' '\n' | tail -2 | tr '\n' ' ')
    echo "$2 $line" | awk '{print "The subdomain " $1 " is a " $2 " record and points to " $3}'
}

if [ "$#" == 1 ]
then
  domain_information "$1" "www"
  domain_information "$1" "lb-01"
  domain_information "$1" "web-01"
  domain_information "$1" "web-02"
elif [ "$#" == 2 ]
then
  domain_information "$1" "$2"
fi
