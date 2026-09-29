# Sulfobutyl Ether Beta-Cyclodextrin (SBE-Beta-CD)

## Key Parameters

- **Degree of substitution (DS): 7**
- **Substitution position:** primary (C6) hydroxyls of all 7 glucose units
- **Counterions (original):** 7 Na⁺
- **Net charge (docking structure):** −7 (Na⁺ removed)
- **SMILES source:** ChemDraw Pro 8.0

## Source

SBE-β-CD was built from a SMILES string exported from **ChemDraw**.
The SMILES was used to generate the 3D structure, and Na⁺ counterions
were removed before docking to keep the cyclodextrin cavity accessible.

- SMILES file: `sbe_beta_cd.smi`
- 3D generation: Avogadro — see pipeline below
- Geometry minimization: MMFF94 (Avogadro)

## Files

| File | Description |
|------|-------------|
| `sbe_beta_cd.smi` | SMILES string exported from ChemDraw (source of truth) |
| `sbe_beta_cd_ds7.pdb` | 3D structure generated from SMILES (includes 7 Na⁺) |
| `sbe_beta_cd_no_na.pdb` | After removing Na⁺ counterions (net charge −7) |
| `sbe_beta_cd_minimized.mol2` | Geometry-minimized structure (MMFF94) |
| `sbe_beta_cd_no_na.mol2` | Na⁺-free structure used as the source for docking / MD |
| `sbe_beta_cd_receptor.pdbqt` | Docking-ready receptor (AutoDock Vina–compatible) |

## Pipeline: ChemDraw → SMILES → 3D → Docking-Ready Receptor

### 1. Structure drawing (ChemDraw)

- β-CD skeleton with 7 sulfobutyl ether groups
  (−O−CH₂−CH₂−CH₂−CH₂−SO₃⁻) attached to the primary (C6) hydroxyls
- 7 Na⁺ counterions added for charge neutrality
- SMILES exported from ChemDraw → `sbe_beta_cd.smi`

### 2. 3D structure generation

- SMILES imported into **Avogadro v2.0.0** → 3D structure generated
- Result saved as `sbe_beta_cd_ds7.pdb`

### 3. Counterion removal

- Na⁺ ions removed to give the biologically relevant anionic form
- Net charge of the resulting molecule: **−7**
- Result saved as `sbe_beta_cd_no_na.pdb`

**Why Na⁺ were removed:**
- The sodium-free form is the active species in aqueous solution
- Na⁺ ions block the cyclodextrin cavity and create false interaction
  sites during docking
- The literature standard for in silico SBE-β-CD studies uses the
  charged, Na⁺-free form

### 4. Geometry optimization (Avogadro)

- Structure opened in Avogadro v2.0.0
- Force field: **MMFF94**
- Algorithm: Steepest Descent (or Conjugate Gradient)
- Result saved as `sbe_beta_cd_minimized.mol2`

### 5. Docking-ready receptor preparation

Prepared using **OpenBabel (Colab)** and cleaned with a short Python script.

```bash
# Step 1 — Convert MOL2 → PDBQT
obabel sbe_beta_cd_no_na.mol2 -O sbe_beta_cd_raw.pdbqt -h --partialcharge gasteiger
```

```python
# Step 2 — Remove ligand-style tags (Vina expects rigid receptors)
with open("sbe_beta_cd_raw.pdbqt", "r") as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    if "ROOT" in line or "BRANCH" in line or "TORSDOF" in line:
        continue
    cleaned_lines.append(line)

with open("sbe_beta_cd_receptor.pdbqt", "w") as f:
    f.writelines(cleaned_lines)
```

- Result: `sbe_beta_cd_receptor.pdbqt` (153 atoms, no ROOT/BRANCH/TORSDOF)

## Software Used

| Tool | Version | Purpose |
|------|---------|---------|
| ChemDraw | Pro 8.0 | Structure drawing + SMILES export |
| Avogadro | 2.0.0 | 3D generation + MMFF94 minimization |
| OpenBabel | 3.1.1 | MOL2 → PDBQT conversion |
| Python | 3.x | Receptor cleanup (tag removal) |
| UCSF ChimeraX | 1.6.1 | Structure inspection |

## Molecule Information

- **Name:** Sulfobutyl ether β-cyclodextrin (SBE-β-CD, DS = 7)
- **Core:** β-cyclodextrin (7 α-D-glucopyranose units, α-(1→4) linkages)
- **Modification:** 7 sulfobutyl ether groups on C6 hydroxyls
- **Counterion (original):** 7 Na⁺
- **Net charge (docking structure):** −7
- **Atoms (docking receptor):** 153

## Assumptions / Notes

- **Degree of substitution (DS) = 7.** Commercial SBE-β-CD (e.g.,
  Captisol®) is typically a mixture with variable DS (average ~6.5–6.8).
  This project models a single representative structure with DS = 7 for
  computational tractability.
- **Substitution pattern:** all sulfobutyl groups on primary (C6)
  hydroxyls, matching the most common synthetic route.
- **Na⁺ counterions were removed** from the docking structure to keep
  the cyclodextrin cavity accessible. The sulfonate groups were retained
  in their deprotonated form (−SO₃⁻). Counterions are reintroduced
  during MD system preparation.
- **Stereochemistry:** taken from the ChemDraw SMILES export.
- **Protonation state:** sulfonate groups deprotonated at pH 7.

## Purpose in This Project

SBE-β-CD is the **modified host** tested against unmodified β-CD to
evaluate the effect of sulfobutyl ether functionalization on curcuminoid
inclusion complexation. Comparison focuses on:

- Curcumin / BDMC binding orientation
- Host–guest interactions
- Complex stability during MD
- Effect of the anionic sulfobutyl groups on the binding

## Role in This Project

Docking and molecular dynamics simulations that use this structure are
documented in `results/docking/` and `notebooks/molecular_dynamics/`.

## References

- ChemDraw: https://www.perkinelmer.com/category/chemdraw
- Avogadro: https://avogadro.cc/
- OpenBabel: https://openbabel.org/
- Das, O., Ghate, V.M., & Lewis, S.A. (2019). Utility of Sulfobutyl
  Ether β-Cyclodextrin Inclusion Complexes in Drug Delivery: A Review.
  *Indian Journal of Pharmaceutical Sciences*, 81(4), 589–600.
- Captisol® (commercial SBE-β-CD): https://www.captisol.com/
