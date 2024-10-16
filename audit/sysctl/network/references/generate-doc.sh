#!/run/current-system/sw/bin/bash

THISDIR=$(dirname "$0")
file1="$THISDIR/reference.csv"
file2="$THISDIR/reference_ipv6.csv"
output_file="$THISDIR/../references.md"

# Create the header row for the Markdown table
header_row="| sysctl configs | expected value | references"
separator_row="|---|---|---|"

# Print the Markdown header to the output file
{
    echo "$header_row"
    echo "$separator_row"
} > "$output_file"

{
    tail -n +1 "$file1" | while IFS=',' read -r line; do
        # Replace commas with pipes for Markdown format
        echo "| $(echo "$line" | tr ',' '|') |"
    done
} >> "$output_file"

# Read and combine data from the second file, skipping the header
{
    tail -n +1 "$file2" | while IFS=',' read -r line; do
        # Replace commas with pipes for Markdown format
        echo "| $(echo "$line" | tr ',' '|') |"
    done
} >> "$output_file"

echo "Markdown table created in $output_file"
