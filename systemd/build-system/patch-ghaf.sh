#!/run/current-system/sw/bin/bash

# Check for required arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <service-bin> <service-tag>"
    echo "Example: $0 ""\"\\$""{pkgs.grafana-alloy}\/bin\/alloy\" \"alloy-tag\""
    echo "Note: '$' and '/' are escape characters, prefix them with '\\'."
    exit 1
fi

THISDIR=$(dirname "$0")
PATCH_FILE="$THISDIR/debug-service.patch"
SERVICEBIN=$1
SERVICETAG=$2

# Replace the pattern in the patch file
sed "s/SERVICEBIN/$SERVICEBIN/g" "$PATCH_FILE" > "./debug-service.patch.temp"
# Check if the sed command succeeded
if [ $? -ne 0 ]; then
    echo "Error! Can not apply service binary."
    exit 1
fi

sed "s/SERVICETAG/$SERVICETAG/g" "./debug-service.patch.temp" > "./ghaf-debug.patch"
# Check if the sed command succeeded
if [ $? -ne 0 ]; then
    echo "Error! Can not apply service tag."
    exit 1
fi

rm "./debug-service.patch.temp"

# Apply the modified patch to the repository
git apply "./ghaf-debug.patch"

# Check if the patch applied successfully
if [ $? -ne 0 ]; then
    echo "Error! Can not apply service tag."
    exit 1
fi

# Check if the git command succeeded
if [ $? -eq 0 ]; then
    echo "Debug patch applied successfully."
    echo "Now you can build Ghaf. Remember service tag to filter the service log."
else
    echo "Error applying the patch."
    exit 1
fi

