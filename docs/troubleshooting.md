## Issue: β-CD `AGLC` residue naming error in the combined MD notebook

**Symptom:** The combined `bcd_only_and_cur_only_MD_100ns.ipynb` notebook 
failed during the `bcd_only` production MD run because the β-CD residues 
were named `AGLC` (CHARMM carbohydrate nomenclature for α-D-glucose), 
and GROMACS could not resolve the residue against the topology.

**Cause:** The Stage-1 input set for `bcd_only` was prepared with an 
inconsistent residue name (`AGLC` in the coordinates but not matching 
the topology entry). This broke `grompp`/`mdrun` at launch.

**Fix:** Re-ran the full Stage-1 workflow (CHARMM-GUI → minimization → 
equilibration) for `bcd_only` with consistent residue naming, then 
re-uploaded the corrected input set to Colab. The corrected 100 ns 
production MD ran cleanly at ~1333 ns/day on Colab A100.

**Working notebook:** `notebooks/MD_simulations_100ns/bcd_cur/bcd_only_MD_100ns.ipynb`

**Failed draft (not uploaded):** combined notebook, `AGLC` residue mismatch.