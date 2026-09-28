# β-Cyclodextrin (β-CD)

## Source

- **SMILES obtained from PubChem**
- PubChem CID: [444041](https://pubchem.ncbi.nlm.nih.gov/compound/444041)
- SMILES file: `beta_cd.smi`

## Files

| File | Description |
|------|-------------|
| `beta_cd.smi` | SMILES string from PubChem (source of truth) |
| `bcd_minimized.pdb` | 3D structure generated from SMILES in Avogadro and MMFF94 geometry optimization (2500 steps) |
| `bcd_minimized_byAutodock.pdbqt` | Docking-ready receptor (AutoDock Tools: polar H + Gasteiger charges) |

## Pipeline: SMILES → 3D → Minimization → Docking

1. **SMILES source:** PubChem CID 444041
2. **3D structure generation:** Avogadro v2.0.0
   - SMILES pasted into Avogadro → 3D coordinates generated
   - Result: `beta_cd_original.pdb`
3. **Geometry optimization:**
   - Tool: Avogadro v2.0.0
   - Force field: MMFF94
   - Steps: 2500
   - Result: `bcd_minimized.pdb`
4. **Preparation for docking:** AutoDock Tools v1.5.7
   - Added polar hydrogens
   - Assigned Gasteiger charges
   - Saved as docking-ready `bcd_minimized_byAutodock.pdbqt`
5. **Molecular docking:** AutoDock Vina (see `results/docking/`)

## Software Used

| Tool | Version | Purpose |
|------|---------|---------|
| PubChem | — | SMILES source (CID 444041) |
| Avogadro | 2.0.0 | 3D generation + MMFF94 minimization |
| AutoDock Tools | 1.5.7 | Docking preparation (H + charges) |
| AutoDock Vina | 1.2.3 | Molecular docking |
| UCSF ChimeraX | 1.6.1 | Structure inspection |

## Molecule Information

- **Name:** β-Cyclodextrin (beta-cyclodextrin)
- **Formula:** C<sub>42</sub>H<sub>70</sub>O<sub>35</sub>
- **Molecular weight:** ~1134.98 g/mol
- **Composition:** Cyclic oligosaccharide of 7 α-D-glucopyranose units
  linked by α-(1→4) glycosidic bonds
- **Rings:** 7 pyranose rings
- **Stereocenters:** All defined (from PubChem canonical SMILES)

## Assumptions / Notes

- No counterions (β-CD is neutral)
- Protonation state: neutral at pH 7
- Stereochemistry: taken from PubChem canonical SMILES (verified)
- No chemical modification applied
- **Geometry optimization was performed** with MMFF94 (2500 steps)
  in Avogadro before docking preparation

## Purpose in This Project

β-CD is used as the **unmodified reference host** for comparative
inclusion complexation with curcumin and BDMC. Results from these
systems (β-CD–CUR, β-CD–BDMC) are compared against SBE-β-CD–CUR
and SBE-β-CD–BDMC to evaluate the effect of sulfobutyl ether
modification on:

- Curcumin / BDMC binding orientation
- Host–guest interactions
- Complex stability during MD simulation

## Role in This Project

Docking and molecular dynamics simulations that use this structure are
documented in `results/docking/` and `notebooks/molecular_dynamics/`.

## References

- PubChem CID 444041: https://pubchem.ncbi.nlm.nih.gov/compound/444041
- Avogadro: https://avogadro.cc/
- AutoDock Tools: https://autodock.scripps.edu/
- AutoDock Vina: https://vina.scripps.edu/