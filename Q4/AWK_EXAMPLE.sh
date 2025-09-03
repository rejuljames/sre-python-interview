#!/bin/bash

# Extract the archive
tar -xzf /home/ubuntu/blahhhhh/archive.tar.gz -C /home/ubuntu/blahhhhh/

# Search for all access logs (assuming .log extension)
find /home/ubuntu/896287-linux-access-log-grouping/ -type f -name "*.log" |
  xargs awk '$1 ~ /^5[0-9][0-9]$/ && $2 != "127.0.0.1" {print $2}' |
  sort | uniq -c | sort -nr | head -n 5 |
  awk '{print $2}' > /tmp/report.log