#!/bin/bash

output_file="passwords_final.txt"
temp_all_passwords="all_passwords.txt"

for file in *.txt; do
    head -n 800 "$file" >> "$temp_all_passwords"
done

sort "$temp_all_passwords" | uniq -c | sort -rn > temp_sorted_passwords.txt

head -n 500 temp_sorted_passwords.txt | awk '{print $2}' > "$output_file"

rm "$temp_all_passwords" temp_sorted_passwords.txt

echo "Most prevalent 100 passwords extracted and saved to $output_file"

