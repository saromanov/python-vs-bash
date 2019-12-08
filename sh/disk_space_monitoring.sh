#!/bin/sh
df -Ph | grep -vE '^Filesystem|tmpfs' | awk '{ print $5,$1 }' | while read output;
do
  max=$1%
  echo $output
  used=$(echo $output | awk '{print $1}')
  partition=$(echo $output | awk '{print $2}')
  if [ ${used%?} -ge ${max%?} ]; then
  echo "The partition \"$partition\" on $(hostname) has used $used at $(date)"
  fi
done