# Curcumin (CUR)

## Key Parameters

- **Molecule type:** Polyphenolic curcuminoid (guest)
- **Source:** PubChem
- **PubChem CID:** [969516](https://pubchem.ncbi.nlm.nih.gov/compound/969516)
- **Net charge (docking structure):** 0 (neutral)
- **Tautomer modeled:** Keto-enol form

## Source

Curcumin was obtained from **PubChem** as an SDF file.
The 3D structure was generated and energy-minimized in Avogadro, and the
resulting structure was prepared for docking using AutoDock Tools.

- SDF file: `Conformer3D_COMPOUND_CID_969516.sdf` (from PubChem)
- SMILES file: `curcumin.smi` (optional — see notes)

## Files

| File | Description |
|------|-------------|
| `Conformer3D_COMPOUND_CID_969516.sdf` | Original SDF file from PubChem (CID: 969516) |
| `curcumin_minimized.mol2` | Geometry-minimized structure (MMFF94, Avogadro) |
| `curcumin_minimized_byAutodock.pdbqt` | Docking-ready ligand (AutoDock Tools: polar H + Gasteiger charges + torsion tree) |

## Pipeline: PubChem → 3D → Minimization → Docking-Ready Ligand

### 1. Structure retrieval (PubChem)

- Downloaded **SDF** file from PubChem CID 969516
- Structure contains the keto-enol tautomer (the thermodynamically
  stable form of curcumin in solution)

### 2. 3D structure generation (Avogadro)

- SDF imported into **Avogadro v2.0.0**
- 3D coordinates generated/verified
- Structure visually inspected in ChimeraX

### 3. Geometry optimization (Avogadro)

- Force field: **MMFF94**
- Algorithm: Steepest Descent (or Conjugate Gradient)
- Steps: [number of steps used, e.g., 2000]
- Result saved as `curcumin_minimized.mol2`

### 4. Ligand preparation for docking (AutoDock Tools v1.5.7)

- Opened `curcumin_minimized.mol2` in **AutoDock Tools**
- Added polar hydrogens
- Assigned Gasteiger charges
- Detected the torsion tree (rotatable bonds) — this tells AutoDock Vina
  which bonds can rotate during docking
- Saved as `curcumin_minimized_byAutodock.pdbqt` (47 atoms)

## Software Used

| Tool | Version | Purpose |
|------|---------|---------|
| PubChem | — | Source of SDF/SMILES (CID 969516) |
| Avogadro | 2.0.0 | 3D generation + MMFF94 minimization |
| AutoDock Tools | 1.5.7 | Docking preparation (H + Gasteiger charges + torsions) |
| AutoDock Vina | 1.2.3 | Molecular docking |
| UCSF ChimeraX | 1.6.1 | Structure inspection |

## Molecule Information

- **Name:** Curcumin (diferuloylmethane)
- **Formula:** C<sub>21</sub>H<sub>20</sub>O<sub>6</sub>
- **Molecular weight:** ~368.38 g/mol
- **Structure:** Two aromatic rings (feruloyl groups) connected by a
  conjugated β-diketone chain
- **Substituents:** Two methoxy (−OCH₃) and two hydroxyl (−OH) groups
  on the aromatic rings
- **Atoms (docking ligand):** 47
- **Tautomer modeled:** Keto-enol form (stable in solution and in the
  solid state)

## Assumptions / Notes

- **Tautomer:** The keto-enol form of curcumin was modeled, consistent
  with its predominant form in solution and with the structure present
  in the PubChem database.
- **Net charge:** 0 (neutral at pH 7). Both hydroxyl groups remain
  protonated in this model.
- **Protonation state:** Neutral.
- **Stereochemistry:** None (curcumin is achiral).
- **Minimization:** Geometry optimized with MMFF94 in Avogadro prior
  to docking preparation.
- **Torsion tree:** Rotatable bonds were detected and configured in
  AutoDock Tools to allow full ligand flexibility during docking.

## Purpose in This Project

Curcumin is one of the two **guest molecules** studied for inclusion
complexation with β-CD and SBE-β-CD. It is the most widely studied
curcuminoid and serves as the reference for comparison against BDMC.

Comparison focuses on:

- Binding orientation inside the host cavity
- Host–guest interactions (H-bonds, hydrophobic contacts)
- Complex stability during MD simulation
- Effect of the methoxy (−OCH₃) groups on binding (CUR vs. BDMC)

## Role in This Project

Docking and molecular dynamics simulations that use this structure are
documented in `results/docking/` and `notebooks/molecular_dynamics/`.

## References

- PubChem CID 969516: https://pubchem.ncbi.nlm.nih.gov/compound/969516
- Avogadro: https://avogadro.cc/
- AutoDock Tools: https://autodock.scripps.edu/
- AutoDock Vina: https://vina.scripps.edu/
