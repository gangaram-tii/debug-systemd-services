#!/bin/bash

# Name of the input CSV file
THISDIR=$(dirname "$0")
reference="references/reference.csv"
reference_ipv6="references/reference_ipv6.csv"

# Name of the output MD file
result="sysctl_audit_result.md"

# Create the header row for the Markdown table
header_row="| sysctl configs | retrieved value | expected value | status | references"
separator_row="|---|---|---|---|---|"

# Print the Markdown header to the output file
{
    echo "$header_row"
    echo "$separator_row"
} > "$result"


# Read the input CSV file
while IFS=, read -r sysctl_config expected_value reference; do
  # Read the corresponding sysctl value from the system
  sysctl_value=$(sysctl -n $sysctl_config)

  # Determine if the sysctl value matches the expected value
  if [[ "$sysctl_value" == "$expected_value" ]]; then
    status="PASS"
  else
    status="FAIL"
  fi

  # Write the data to the output CSV file
  echo "| $sysctl_config | $sysctl_value | $expected_value | $status | $reference |" >> "$result"
done < "$reference"


ipv6_disabled=$(sysctl -n net.ipv6.conf.all.disable_ipv6)
if [[ "$ipv6_disabled" == "0" ]]; then
  # Read the input CSV file
  while IFS=, read -r sysctl_config expected_value reference; do
    # Read the corresponding sysctl value from the system
    sysctl_value=$(sysctl -n $sysctl_config)

    # Determine if the sysctl value matches the expected value
    if [[ "$sysctl_value" == "$expected_value" ]]; then
      status="PASS"
    else
      status="FAIL"
    fi

    # Write the data to the output CSV file
    echo "| $sysctl_config | $sysctl_value | $expected_value | $status | $reference |" >> "$result"
  done < "$reference_ipv6"

fi

echo "DDDDDDDDDDDDDDD"