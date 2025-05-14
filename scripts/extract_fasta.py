import os
from rnapolis.parser import read_3d_structure
from rnapolis.annotator import extract_secondary_structure

def extract_fasta(input_file, output_file):
    with open(input_file, 'r') as infile:
        struct = read_3d_structure(infile, 1)
        struct2d = extract_secondary_structure(struct, 1)
    sequences = struct2d[1][0].split('\n')[1::3]
    return sequences


def main():
    pdb_dir = "/home/mjustyna/data/rna-solo"
    files = os.listdir(pdb_dir)
    files = [f for f in files if f.endswith(".pdb")]
    for file in files:
        input_file = os.path.join(pdb_dir, file)
        output_file = os.path.join(pdb_dir, f"{file}.fasta")
        extract_fasta(input_file, output_file)
        print(f"Extracted FASTA from {input_file} to {output_file}")

if __name__ == "__main__":
    main()