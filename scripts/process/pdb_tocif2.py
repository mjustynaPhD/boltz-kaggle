import gemmi

input_struct = "/home/mjustyna/data/rna-solo/8FZA_1_A.pdb"
out = "/home/mjustyna/data/rna-test-cif/8FZA_1_A.cif"
# Read the PDB
structure = gemmi.read_structure(input_struct)

# Save it as mmCIF with basic metadata
structure.setup_entities()  # this populates entity and chain info
structure.assign_label_seq_id()  # optional, improves labeling
print(structure.entities[0].full_sequence)
structure.make_mmcif_document().write_file(out)