#!/bin/bash

additional_files="all_passwords/*.txt" 

cat $additional_files | awk '!seen[$0]++' >> passwords_final.txt

