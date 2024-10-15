#!/run/current-system/sw/bin/bash

# Define the path to the audit log
AUDIT_LOG="/var/log/audit/audit.log"

# Get the key to search for from the command-line argument
if [ $# -eq 0 ]; then
    echo "Please provide a service tag to filter the log."
    exit 1
fi

SEARCH_KEY=$1

# Declare an associative array to track unique syscalls
declare -A seen_syscalls

# Read the entire audit log file
while read -r line; do
    # Check if the line contains both the search key and a system call entry
    if echo "$line" | grep -q "type=SYSCALL" && echo "$line" | grep -q "$SEARCH_KEY"; then
        # Extract the syscall name
        syscall=$(echo "$line" | grep -oP 'SYSCALL=\K\w+')

        # Check if this syscall has already been seen
        if [[ -z "${seen_syscalls[$syscall]}" ]]; then
            # If not seen, print the syscall and mark it as seen
            echo "$syscall"
            seen_syscalls[$syscall]=1
        fi
    fi
done < "$AUDIT_LOG"
