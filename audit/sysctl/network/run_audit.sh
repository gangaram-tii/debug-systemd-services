#!/run/current-system/sw/bin/bash

# Name of the input CSV file
THISDIR=$(dirname "$0")
reference="$THISDIR/references/reference.csv"
reference_ipv6="$THISDIR/references/reference_ipv6.csv"

# Name of the output MD file
result="sysctl_network_audit_report.md"

# Create the header row for the Markdown table
header_row="| index | sysctl configs | retrieved value | expected value | status | references"
separator_row="|---|---|---|---|---|---|"

# Print the Markdown header to the output file
{
    echo "# Audit report: network hardening using sysctl"
    echo "$header_row"
    echo "$separator_row"
} > "$result"

index=0
# Read the input CSV file
while IFS=, read -r sysctl_config expected_value reference; do
  # Read the corresponding sysctl value from the system
  sysctl_value=$(sysctl -n $sysctl_config)
  index=$((index + 1))
  # Determine if the sysctl value matches the expected value
  if [[ " $sysctl_value " == "$expected_value" ]]; then
    status="OK"
  else
    status="NOK"
  fi

  # Write the data to the output CSV file
  echo "| $index | $sysctl_config | $sysctl_value | $expected_value | $status | $reference |" >> "$result"
done < "$reference"


ipv6_disabled=$(sysctl -n net.ipv6.conf.all.disable_ipv6)
if [[ "$ipv6_disabled" == "0" ]]; then
  # Read the input CSV file
  while IFS=, read -r sysctl_config expected_value reference; do
    # Read the corresponding sysctl value from the system
    sysctl_value=$(sysctl -n $sysctl_config)
    index=$((index + 1))
    # Determine if the sysctl value matches the expected value
    if [[ " $sysctl_value " == "$expected_value" ]]; then
      status="OK"
    else
      status="NOK"
    fi

    # Write the data to the output CSV file
    echo "| $index | $sysctl_config | $sysctl_value | $expected_value | $status | $reference |" >> "$result"
  done < "$reference_ipv6"

fi
