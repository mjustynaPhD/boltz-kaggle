from pathlib import Path

# Paths to your folders
pdb_folder = Path("/home/mjustyna/data/rna-solo/")
pkl_folder = Path("ccd/mols/")

# Get all PDB filenames (without extension)
pdb_files = {f.stem for f in pdb_folder.glob("*.pdb")}

# Get all pickle filenames (without extension)
pkl_files = {f.stem for f in pkl_folder.glob("*.pkl")}

# Find PDBs without matching pickle
missing_pickles = pdb_files - pkl_files

print(f"Missing pickles for {len(missing_pickles)} files:")
for name in sorted(missing_pickles):
    print(name)

# Optional: remove them from your PDB folder
for name in missing_pickles:
    file_to_remove = pdb_folder / f"{name}.pdb"
    file_to_remove.unlink()  # comment this line if you just want to preview
    print(f"Removed {file_to_remove}")