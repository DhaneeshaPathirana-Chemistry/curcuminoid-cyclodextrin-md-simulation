# Bisdemethoxycurcumin (BDMC)

## Overview

- **Molecule type:** Polyphenolic curcuminoid (guest)
- **Source:** PubChem
- **PubChem CID:** [5315472](https://pubchem.ncbi.nlm.nih.gov/compound/5315472)
- **Net charge (docking structure):** 0 (neutral)
- **Tautomer modeled:** Keto-enol form

## Source

BDMC was obtained from **PubChem** as a PDB file.
The structure was energy-minimized in Avogadro, and the resulting
structure was prepared for docking using AutoDock Tools.

- PDB file: `bdmc.pdb` (from PubChem)
- SMILES file: `bdmc.smi` (optional)

## Files

| File | Description |
|------|-------------|
| `bdmc.pdb` | Original PDB file from PubChem (CID: 5315472) |
| `bdmc_minimized.mol2` | Geometry-minimized structure (MMFF94, Avogadro) |
| `bdmc_minimized_byAutodock.pdbqt` | Docking-ready ligand (AutoDock Tools: polar H + Gasteiger charges + torsion tree) |

## Pipeline: PubChem → 3D → Minimization → Docking-Ready Ligand

### 1. Structure retrieval (PubChem)

- Downloaded **PDB** file from PubChem CID 5315472
- Structure contains the keto-enol tautomer (the thermodynamically
  stable form of BDMC)

### 2. 3D structure generation (Avogadro)

- PDB file imported into **Avogadro v2.0.0**
- 3D coordinates verified
- Structure visually inspected in ChimeraX

### 3. Geometry optimization (Avogadro)

- Force field: **MMFF94**
- Algorithm: Steepest Descent (or Conjugate Gradient)
- Steps: [number of steps used]
- Result saved as `bdmc_minimized.mol2`

### 4. Ligand preparation for docking (AutoDock Tools v1.5.7)

- Opened `bdmc_minimized.mol2` in **AutoDock Tools**
- Added polar hydrogens
- Assigned Gasteiger charges
- Detected the torsion tree (rotatable bonds) — this tells AutoDock Vina
  which bonds can rotate during docking
- Saved as `bdmc_minimized_byAutodock.pdbqt`

## Software Used

| Tool | Version | Purpose |
|------|---------|---------|
| PubChem | — | Source of PDB file (CID 5315472) |
| Avogadro | 2.0.0 | 3D verification + MMFF94 minimization |
| AutoDock Tools | 1.5.7 | Docking preparation (H + Gasteiger charges + torsions) |
| AutoDock Vina | 1.2.3 | Molecular docking |
| UCSF ChimeraX | 1.6.1 | Structure inspection |

## Molecule Information

- **Name:** Bisdemethoxycurcumin (BDMC)
- **Formula:** C<sub>19</sub>H<sub>16</sub>O<sub>4</sub>
- **Molecular weight:** ~308.33 g/mol
- **Structure:** Two aromatic rings (coumaroyl groups) connected by a
  conjugated β-diketone chain
- **Substituents:** Two hydroxyl (−OH) groups on the aromatic rings
  (no methoxy groups, unlike curcumin)
- **Atoms (docking ligand):** ~43
- **Tautomer modeled:** Keto-enol form

## Assumptions / Notes

- **Tautomer:** The keto-enol form of BDMC was modeled, consistent with
  its predominant form in solution and with the structure present in
  the PubChem database.
- **Net charge:** 0 (neutral at pH 7). Both hydroxyl groups remain
  protonated in this model.
- **Protonation state:** Neutral.
- **Stereochemistry:** None (BDMC is achiral).
- **Key structural difference from curcumin:** BDMC lacks the two
  methoxy (−OCH₃) groups present in curcumin, making it slightly
  smaller and less hindered. This is the primary structural variable
  being tested in this comparative study.
- **Minimization:** Geometry optimized with MMFF94 in Avogadro prior
  to docking preparation.
- **Torsion tree:** Rotatable bonds were detected and configured in
  AutoDock Tools to allow full ligand flexibility during docking.

## Purpose in This Project

BDMC is one of the two **guest molecules** studied for inclusion
complexation with β-CD and SBE-β-CD. It is a demethoxy analogue of
curcumin, and serves as the direct structural comparison to curcumin.

The key scientific question is: **How does the absence of the two
methoxy (−OCH₃) groups affect inclusion complexation with β-CD and
SBE-β-CD?**

Comparison focuses on:

- Binding orientation inside the host cavity
- Host–guest interactions (H-bonds, hydrophobic contacts)
- Complex stability during MD simulation
- Effect of removing −OCH₃ groups on binding (BDMC vs. CUR)

## Role in This Project

Docking and molecular dynamics simulations that use this structure are
documented in `results/docking/` and `notebooks/molecular_dynamics/`.

## References

- PubChem CID 5315472: https://pubchem.ncbi.nlm.nih.gov/compound/5315472
- Avogadro: https://avogadro.cc/
- AutoDock Tools: https://autodock.scripps.edu/
- AutoDock Vina: https://vina.scripps.edu/