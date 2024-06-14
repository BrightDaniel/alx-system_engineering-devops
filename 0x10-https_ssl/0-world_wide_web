#!/usr/bin/env bash
# Script that will display information about subdomains

DNS_info () {
    ANSWER=$(dig $2 | grep -A1 'ANSWER SECTION:' | awk 'NR==2 {print $0}')
    echo "The subdomain $1 is a $(echo $ANSWER | awk '{print $4}') record and points to $(echo $ANSWER | awk '{print $5}')"
}

if [[ $# == 1 ]]; then
    subdomains=('www' 'lb-01' 'web-01' 'web-02')
    for i in "${subdomains[@]}"; do
	CONCAT="$i.$1"
	DNS_info $i $CONCAT
    done
else
    CONCAT="$2.$1"
    DNS_info $2 $CONCAT
fi
