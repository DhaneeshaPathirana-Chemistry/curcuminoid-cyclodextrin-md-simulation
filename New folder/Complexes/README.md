# Complex Structures for MD Simulation

Host–guest inclusion complexes prepared as input structures for
molecular dynamics simulations in GROMACS via CHARMM-GUI.

## Purpose

Each complex contains one cyclodextrin host (β-CD or SBE-β-CD) and
curcumin in the binding pose obtained from molecular docking. These
structures were prepared with correct residue naming, chain
identifiers, atom typing, and bond orders so that CHARMM-GUI's
Ligand Reader & Modeler could parameterize them successfully for MD
simulation.

## Systems

Two systems have been prepared for MD simulation at this stage:

| System | Host (Chain) | Guest (Chain) | Complex PDB | Box size | Status |
|--------|--------------|---------------|-------------|----------|--------|
| 1 | β-CD (B) | Curcumin (A) | `cur_bcd_complex.pdb` | 34.9 Å | Prepared |
| 2 | SBE-β-CD (S) | Curcumin (A) | `cur_sbe_complex.pdb` | (generating) | In progress |

Systems involving bisdemethoxycurcumin (BDMC) are planned for the next
stage of the project.

## Preparation Workflow

Each complex was prepared in **UCSF ChimeraX** using the following
workflow:

### 1. Best-pose extraction (ChimeraX)

The best docking pose (Pose 1) was extracted from each docking result
as documented in `results/best_poses/README.md`. This produced one
curcumin best-pose PDB file per system.

### 2. Complex building (ChimeraX — DockPrep)

In ChimeraX:

1. The curcumin best-pose PDB was opened together with the receptor
   structure used in docking:
   - β-CD system → `bcd_minimized_byAutodock.pdbqt`
   - SBE-β-CD system → `sbe_beta_cd_receptor.pdbqt`
2. The **DockPrep** tool in ChimeraX was used to prepare and combine
   the host and curcumin into a single complex. DockPrep:
   - Added hydrogens
   - Assigned partial charges
   - Standardized atom and residue names
3. The prepared complex was saved as a PDB file.

### 3. Residue naming and file preparation (Sublime Text)

For each complex, the PDB file was opened in a text editor and edited
to make it acceptable for CHARMM-GUI:

- **Residue names** were changed from `UNL` to meaningful names
  (see Residue Names table below)
- **Chain identifiers** were added or corrected at column 22
  (see Chain IDs table below)
- **Residue numbers** were made distinct (guest = 1, host = 2)
- **TER** cards were added between the two chains
- **MODEL / ENDMDL** lines were removed (CHARMM-GUI expects a single
  model)
- **Atom numbering** was verified to be continuous
- **Bond orders** were manually checked and, where necessary, adjusted

### 4. Ligand MOL2 preparation (Sublime Text)

Separate MOL2 files were prepared for the **host** and **guest** to
provide CHARMM-GUI with the chemical connectivity (bond orders and
atom types) required for CGenFF parameterization.

For each MOL2 file:

- **Molecule name** was set to a simple identifier
- **Residue names** were updated to match the PDB file
- **Atom types** were verified
- **Bond orders** were checked and corrected where necessary
- **SUBSTRUCTURE** section was updated to match the residue name

## CHARMM-GUI Input Files

For each prepared system, **three input files** were submitted to
CHARMM-GUI Solution Builder:

| File type | Purpose |
|-----------|---------|
| Complex PDB | 3D coordinates of the host–guest complex |
| Guest MOL2 | Connectivity for the guest ligand (CGenFF parameterization) |
| Host MOL2 | Connectivity for the host molecule (CGenFF parameterization) |

### File matrix

| System | Complex PDB | Guest MOL2 | Host MOL2 |
|--------|-------------|------------|-----------|
| 1. CUR + β-CD | `cur_bcd_complex.pdb` | `curcumin.mol2` | `bcd.mol2` |
| 2. CUR + SBE-β-CD | `cur_sbe_complex.pdb` | `curcumin.mol2` | `sbe_bcd.mol2` |

**Note:** The guest MOL2 file (`curcumin.mol2`) is reused across both
systems because the guest molecule is the same.

### CHARMM-GUI settings

Each submission used the following settings:

| Parameter | Value |
|-----------|-------|
| Input method | Upload PDB file |
| Ligand parameterization | CGenFF via uploaded MOL2 files |
| Guess bond orders from connectivity | Checked |
| Force field | CHARMM36m |
| Water box | Rectangular |
| Water buffer | 10 Å |
| Salt | 0.15 M NaCl |
| Temperature | 298 K |
| Ensembles | NVT (equilibration) + NPT (production) |
| Output engine | GROMACS |

**Note on water box size:** CHARMM-GUI automatically calculates the
final box dimensions based on the size of the complex plus the 10 Å
buffer. For the CUR + β-CD system, the resulting box was
**34.9 Å × 34.9 Å × 34.9 Å**. The corresponding box for the
CUR + SBE-β-CD system is being generated.

CHARMM-GUI generated the MD-ready GROMACS input files for both
systems (see `notebooks/molecular_dynamics/README.md`).

## Files

### Complex PDB files (ChimeraX output)

| File | Description |
|------|-------------|
| `cur_bcd_complex.pdb` | Curcumin + β-CD complex |
| `cur_sbe_complex.pdb` | Curcumin + SBE-β-CD complex |

### Host and guest MOL2 files

| File | Molecule | Used for system(s) |
|------|----------|---------------------|
| `curcumin.mol2` | Curcumin | 1, 2 |
| `bcd.mol2` | β-Cyclodextrin | 1 |
| `sbe_bcd.mol2` | SBE-β-CD | 2 |

## Software Used

| Tool | Version | Purpose |
|------|---------|---------|
| UCSF ChimeraX | 1.6.1 | Best-pose extraction, DockPrep, complex building |
| Sublime Text | — | PDB/MOL2 manual editing and cleanup |
| CHARMM-GUI | — | MD system preparation and GROMACS input generation |

## Verification

Each complex was verified before submission to CHARMM-GUI:

- Both host and curcumin visible when opened in ChimeraX
- Curcumin located inside the host cavity
- No broken bonds or missing atoms
- Correct residue names and chain IDs
- No `MODEL` / `ENDMDL` lines remaining
- Continuous atom numbering
- `TER` card present between chains

## Residue Names

Residue names were assigned to uniquely identify each molecule in the
complex, as required by CHARMM-GUI's Ligand Reader & Modeler:

| Molecule | Residue name | Notes |
|----------|--------------|-------|
| Curcumin | `CUR` | Guest |
| β-Cyclodextrin | `BCD` | Host |
| SBE-β-CD | `SBE` | Host |

## Chain IDs

Chain IDs were assigned to distinguish the host and guest molecules
within each complex:

| Chain ID | Molecule | Role |
|----------|----------|------|
| `A` | Curcumin (CUR) | Guest |
| `B` | β-Cyclodextrin (BCD) | Host |
| `S` | SBE-β-CD (SBE) | Host |

Using different chain IDs for each molecule is required by CHARMM-GUI
to correctly distinguish and parameterize the two components of the
complex.

## Notes

### CONECT records removed during complex preparation

When the host and guest were combined using **DockPrep** in ChimeraX,
the **CONECT records** (which define interatomic bond connectivity)
were **not preserved** in the output complex PDB file.

This is expected behavior for the DockPrep workflow, which prioritizes
the 3D coordinates and atom identifiers over bond information. Because
CHARMM-GUI's Ligand Reader & Modeler rebuilds connectivity from the
MOL2 files, this did not affect the parameterization step.

**Implication:** The complex PDB files contain coordinates and atom
identities but not explicit bond information. The chemical
connectivity is provided separately by the MOL2 files uploaded to
CHARMM-GUI.

### Manual bond order adjustment

During MOL2 preparation, some double bonds were found to be rendered
as single bonds. These were manually corrected in the MOL2 files to
ensure correct connectivity for CGenFF parameterization.

### Hypervalent carbon issue in curcumin

The CGenFF parameterization initially failed for curcumin with the
error:
attype warning: hypervalent carbon (valence = 5) (C9) not supported


This was resolved by manually adjusting the bond order of the C9–C10
bond in the curcumin MOL2 file so that C9 had a chemically valid
valence of 4. Full details are documented in
`docs/troubleshooting.md`.

## Next Step

The two prepared complexes were submitted to **CHARMM-GUI Solution
Builder** to generate GROMACS input files. The MD setup and simulation
workflow is documented in `notebooks/molecular_dynamics/README.md`.

Complexes involving bisdemethoxycurcumin (BDMC) will be prepared and
submitted in a later stage following the same workflow.

## References

- Jo, S., Kim, T., Iyer, V.G., & Im, W. (2008). CHARMM-GUI: A web-based
  graphical user interface for CHARMM. *Journal of Computational
  Chemistry*, 29(11), 1859–1865.
- CHARMM-GUI: https://www.charmm-gui.org/
- UCSF ChimeraX: https://www.rbvi.ucsf.edu/chimerax/