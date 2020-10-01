#!/bin/bash

# cleans up and formats /guy_gold/ansible/inventories/all,
# to serve as python dict file.

INPUT_FILE="/bg_guy_gold/ansible/inventories/all" 
OUTPUT_FILE="hosts_dict.py"


# some 'sed' steps might be redundant, however, they do guarantee a resulting 
# python dictionary in case of anomalies in the source file

sed '
s/\#spare.*$// 
s/^#.*//
s/[[:space:]]*ansible_host=/: /  
s/^\[zone.*// 
s/^\[phase.*//
s/^zone.*// 
s/\[.*\]//
s/BGROBOT.*//
/^[[:space:]]*$/d
s/^/"/
s/$/"/
s/: /": "/
s/$/,/
' "$INPUT_FILE" > "$OUTPUT_FILE"

# final additions of text, better done outside of the main 'sed' routine
sed -i '1 i\my_dict = {' "$OUTPUT_FILE"
echo "}" >> "$OUTPUT_FILE"

