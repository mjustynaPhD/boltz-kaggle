#!/bin/bash

CIF_DIR="/home/mjustyna/data/rna-solo-cifs/"
# Output file
output_file="component.cif"
> "$output_file"  # Clear or create output file

# Initialize counter
counter=0

# Sort input files alphabetically for consistency
for cif_file in $(ls $CIF_DIR/*.cif | sort); do
    #  printf "data_%04d\n#\n" "$counter" >> "$output_file"

    # Append the contents of the cif file
    cat "$cif_file" >> "$output_file"

    # Separate entries with a newline (optional)
    echo -e "\n" >> "$output_file"

    # Increment counter
    ((counter++))
done