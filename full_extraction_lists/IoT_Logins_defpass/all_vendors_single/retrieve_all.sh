#!/bin/bash

# Directory to store the output files
output_dir="output"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# File containing the list of names (one per line)
names_file="vendors.txt"

# Iterate over each name in the file
while IFS= read -r name; do
    # Remove leading/trailing whitespace from the name
    name=$(echo "$name" | awk '{$1=$1};1')

    # Generate the query URL by replacing the query placeholder with the name
    query_url="https://defpass.com/index.php"
    query_data="--data \"query=$name\""

    # Generate the output filename based on the query
    output_file="$output_dir/${name}.html"

    # Execute the curl command and write the HTML output to the file
    curl_command="curl -s -X POST -H \"Host: defpass.com\" -H \"Cache-Control: max-age=0\" -H \"Upgrade-Insecure-Requests: 1\" -H \"Origin: https://defpass.com\" -H \"Content-Type: application/x-www-form-urlencoded\" -H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36\" -H \"Referer: https://defpass.com/index.php\" $query_data \"$query_url\""
    
    # Execute the curl command and write the HTML output to the file
    eval "$curl_command" > "$output_file"
    
    echo "HTML output for query '$name' saved to $output_file"

    sleep 2

done < "$names_file"


# sqlmap --url "https://defpass.com/index.php" --method POST --data "query=Samsung" --technique BEUSQ --banner --random-agent -o --threads 5 