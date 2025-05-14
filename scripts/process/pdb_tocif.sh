#!/bin/bash

PDBS="/home/mjustyna/data/rna-solo/"
OUT="/home/mjustyna/data/rna-solo-cifs/"

mkdir -p $OUT

for pdb_file in $PDBS/*.pdb; do
    # Get the base filename without extension
    echo "Processing $pdb_file"
    base_name=$(basename "$pdb_file" .pdb)

    # Define output path
    cif_file="${OUT}/${base_name}.cif"

    # Convert using pdb-tools
    pdb_tocif "$pdb_file" > "$cif_file"

    echo "Converted $pdb_file -> $cif_file"
done