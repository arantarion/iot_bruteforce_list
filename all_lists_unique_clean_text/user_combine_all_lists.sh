#!/bin/bash

additional_files="all_users/*.txt" 

cat $additional_files | awk '!seen[$0]++' >> users_final.txt


