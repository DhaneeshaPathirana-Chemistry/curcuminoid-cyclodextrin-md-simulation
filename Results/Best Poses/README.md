# Best Docking Poses

The best binding pose (Pose 1) extracted from each docking result,
selected for downstream complex building and MD simulation setup.

## Purpose

After molecular docking with AutoDock Vina, each docking run produces
multiple binding poses (typically 10) ranked by predicted binding
affinity. This folder contains the **single best pose** from each
system, extracted and saved as an individual structure file.

These best-pose files are the starting point for building the
host–guest complex that will be used as input for molecular dynamics
simulations.

## Systems and Best Poses

| System | Grid size | Pose 1 binding affinity (kcal/mol) |
|--------|-----------|-------------------------------------|
| Curcumin + β-CD | 14 Å | −5.376 |
| BDMC + β-CD | 14 Å | −5.170 |
| Curcumin + SBE-β-CD | 18 Å | −5.082 |
| BDMC + SBE-β-CD | 18 Å | −4.777 |

## Files

| File | Description |
|------|-------------|
| `cur_bcd_best_pose.pdb` | Best pose of curcumin in β-CD |
| `bdmc_bcd_best_pose.pdb` | Best pose of BDMC in β-CD |
| `cur_sbe_best_pose.pdb` | Best pose of curcumin in SBE-β-CD |
| `bdmc_sbe_best_pose.pdb` | Best pose of BDMC in SBE-β-CD |

## Extraction Method

For each system:

1. The docking result file (containing multiple poses) was opened in
   **UCSF ChimeraX** (File → Open → select the `.pdbqt` file).

   This loads all generated poses as separate models in the
   **Models** panel (labeled `#1.1` through `#1.10` for the standard
   10-pose AutoDock Vina output).

2. In the **Models** panel, all pose models except the first one
   (Pose 1, corresponding to the lowest binding energy) were manually
   deselected or hidden, so that only the best pose remained visible.

3. The best pose was saved separately:
   - **File → Save** (or **Save As**)
   - Format: **PDB**
   - Filename: `<system>_best_pose.pdb`
   - Only the currently visible/selected model was saved.

4. The saved best-pose file was visually inspected to confirm the
   guest molecule is located **inside** the host cavity (not floating
   outside).

The extraction was performed interactively through the ChimeraX
graphical interface; no command-line input was used.

## Source Docking Results

The best pose was extracted from the following docking result files
(see `results/docking/README.md` for details):

| Best pose | Source docking result |
|-----------|------------------------|
| `cur_bcd_best_pose.pdb` | `cur_bcd_docked_14A.pdbqt` |
| `bdmc_bcd_best_pose.pdb` | `bdmc14_bcd_docked.pdbqt` |
| `cur_sbe_best_pose.pdb` | `cur_sbe_docked.pdbqt` |
| `bdmc_sbe_best_pose.pdb` | `bdmc_sbe_docked18.pdbqt` |

## Software Used

| Tool | Version | Purpose |
|------|---------|---------|
| UCSF ChimeraX | 1.6.1 | Pose extraction and visualization |
| AutoDock Vina | 1.2.3 | Source of docking results |

## Notes

- Each best-pose file contains **only the guest molecule** (curcumin
  or BDMC) in its final docked geometry. The host structure is not
  included — it is added separately when building the MD-ready complex
  (see `results/complexes/`).
- Pose 1 is defined as the pose with the most negative (i.e., most
  favorable) binding affinity, following the standard AutoDock Vina
  output convention.
- All 4 best poses were verified visually in ChimeraX before being
  saved.

## Next Step

These best-pose files are used to build the complete host–guest
complexes for MD simulation. See `results/complexes/` for the merged
complex structures.