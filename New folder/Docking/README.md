# Docking Results

Comparative docking of curcumin (CUR) and bisdemethoxycurcumin (BDMC)
into β-cyclodextrin (β-CD) and sulfobutyl ether β-cyclodextrin
(SBE-β-CD) using AutoDock Vina.

## Systems Studied

| System | Host | Guest | Abbreviation |
|--------|------|-------|--------------|
| 1 | β-Cyclodextrin | Curcumin | CUR + β-CD |
| 2 | β-Cyclodextrin | Bisdemethoxycurcumin | BDMC + β-CD |
| 3 | SBE-β-Cyclodextrin | Curcumin | CUR + SBE-β-CD |
| 4 | SBE-β-Cyclodextrin | Bisdemethoxycurcumin | BDMC + SBE-β-CD |

## Docking Parameters

All dockings were performed using **AutoDock Vina v1.2.3** on Google Colab.

| Parameter | β-CD systems | SBE-β-CD systems |
|-----------|--------------|-------------------|
| Receptor | `bcd_minimized_byAutodock.pdbqt` | `sbe_beta_cd_receptor.pdbqt` |
| Ligand (CUR) | `curcumin_minimized_byAutodock.pdbqt` | same |
| Ligand (BDMC) | `bdmc_minimized_byPyRx.pdbqt` | same |
| Grid center X | −0.01 | 3.34 |
| Grid center Y | −0.00 | −0.60 |
| Grid center Z | 0.01 | −2.69 |
| Grid size | 14 × 14 × 14 Å | 18 × 18 × 18 Å |
| Spacing | 0.375 Å (default) | 0.375 Å (default) |
| Exhaustiveness | 16 | 16 |
| Number of modes | 10 | 10 |
| Scoring function | vina | vina |

**Notes on grid parameters:**

- For **β-CD**, the grid center was set to the geometric center of the
  β-CD cavity, measured in ChimeraX.
- For **SBE-β-CD**, the center of mass of the SBE-β-CD molecule was
  used (3.34, −0.60, −2.69 Å) because the SMILES-generated structure
  was placed at a different position in coordinate space than the
  original β-CD.
- **Grid box size** was optimized separately for each host (see below).
  β-CD systems used 14 Å; SBE-β-CD systems used 18 Å.

## Grid Box Optimization

Multiple grid box sizes were tested for each host to identify the
optimal search space.

### β-CD systems (host cavity ~15 Å wide)

| Grid size | CUR + β-CD (kcal/mol) | BDMC + β-CD (kcal/mol) |
|-----------|------------------------|-------------------------|
| 14 Å | −5.376 | −5.170 |
| 16 Å | −5.297 | — |
| 18 Å | −5.357 | — |
| 22 Å | — | — |

**Conclusion:** 14 Å was selected as the final grid box size for both
β-CD systems. The three tested sizes (14, 16, 18 Å) all gave
consistent results in the −5.3 to −5.4 kcal/mol range, confirming
convergence.

### SBE-β-CD systems (host cavity with bulkier chains)

| Grid size | CUR + SBE-β-CD (kcal/mol) | BDMC + SBE-β-CD (kcal/mol) |
|-----------|---------------------------|-----------------------------|
| 14 Å | −4.552 (unstable) | −5.068 |
| 18 Å | **−5.082** | **−4.777** |
| 22 Å | −4.505 | — |

**Conclusion:** 18 Å was selected as the final grid box size for both
SBE-β-CD systems.

- The **22 Å** box was too large — the ligand could explore outside
  the cavity and weaker binding resulted.
- The **14 Å** box was too tight for curcumin (poses 9 and 10 gave
  positive energies, indicating the ligand could not fit). BDMC,
  which is smaller, gave a reasonable result at 14 Å but 18 Å was
  chosen for consistency with the CUR + SBE-β-CD system.
- The **18 Å** box gives a physically reasonable search area that
  accommodates the flexible sulfobutyl ether side chains of SBE-β-CD
  while keeping the ligand inside the cavity.

## Final Results

| Rank | System | Grid Size | Best Binding Affinity (kcal/mol) |
|------|--------|-----------|----------------------------------|
| 1 | CUR + β-CD | 14 Å | **−5.376** |
| 2 | BDMC + β-CD | 14 Å | **−5.170** |
| 3 | CUR + SBE-β-CD | 18 Å | **−5.082** |
| 4 | BDMC + SBE-β-CD | 18 Å | **−4.777** |

All four systems show **negative binding energies**, indicating
spontaneous and favorable inclusion complexation.

## Host Effect (β-CD vs. SBE-β-CD)

| Guest | β-CD (kcal/mol) | SBE-β-CD (kcal/mol) | Δ | Observation |
|-------|------------------|----------------------|---|-------------|
| Curcumin | −5.376 | −5.082 | −0.294 | β-CD better |
| BDMC | −5.170 | −4.777 | −0.393 | β-CD better |

**Observation:** β-CD binds both guests more strongly than SBE-β-CD
in the docking calculations. This is consistent with the literature,
where the charged sulfobutyl ether groups may interfere with
hydrophobic encapsulation of neutral curcuminoid guests.

## Guest Effect (Curcumin vs. BDMC)

| Host | Curcumin (kcal/mol) | BDMC (kcal/mol) | Δ | Observation |
|------|---------------------|------------------|---|-------------|
| β-CD | −5.376 | −5.170 | −0.206 | CUR better |
| SBE-β-CD | −5.082 | −4.777 | −0.305 | CUR better |

**Observation:** Curcumin binds more strongly than BDMC in both hosts.
The two methoxy (−OCH₃) groups present in curcumin (but absent in
BDMC) appear to contribute favorable hydrophobic interactions within
the cavity. This is consistent with the literature, where native β-CD
provides a superior geometric fit for curcumin compared to its
demethoxy analogue.

## Files

### Final Docking Result Files

| File | Description |
|------|-------------|
| `cur_bcd_docked_14A.pdbqt` | Docked poses: Curcumin + β-CD (14 Å) |
| `cur_bcd_log_14A.txt` | Vina log: Curcumin + β-CD (14 Å) |
| `bdmc14_bcd_docked.pdbqt` | Docked poses: BDMC + β-CD (14 Å) |
| `bdmc14_bcd_log.txt` | Vina log: BDMC + β-CD (14 Å) |
| `cur_sbe_docked.pdbqt` | Docked poses: Curcumin + SBE-β-CD (18 Å) |
| `cur_sbe_log.txt` | Vina log: Curcumin + SBE-β-CD (18 Å) |
| `bdmc_sbe_docked18.pdbqt` | Docked poses: BDMC + SBE-β-CD (18 Å) |
| `bdmc_sbe_log18.txt` | Vina log: BDMC + SBE-β-CD (18 Å) |

### Grid Optimization Trial Files

| File | Description |
|------|-------------|
| `cur_bcd_docked_16A.pdbqt` | Trial: Curcumin + β-CD (16 Å) |
| `cur_bcd_log_16A.txt` | Vina log (16 Å trial) |
| `cur_bcd_docked_18A.pdbqt` | Trial: Curcumin + β-CD (18 Å) |
| `cur_bcd_log_18A.txt` | Vina log (18 Å trial) |
| `cur_sbe_docked22.pdbqt` | Trial: Curcumin + SBE-β-CD (22 Å) |
| `cur_sbe_log22.txt` | Vina log (22 Å trial) |
| `cur_sbe_docked0.pdbqt` | Trial: Curcumin + SBE-β-CD (center 0,0,0) |
| `cur_sbe_log0.txt` | Vina log (center 0,0,0 trial) |
| `cur_sbe_docked14.pdbqt` | Trial: Curcumin + SBE-β-CD (14 Å, unstable) |
| `cur_sbe_log14.txt` | Vina log (14 Å trial) |
| `bdmc_sbe_docked14.pdbqt` | Trial: BDMC + SBE-β-CD (14 Å) |
| `bdmc_sbe_log14.txt` | Vina log (14 Å trial) |

## Methods

### Receptor preparation

Receptor preparation is documented in:

- `structures/hosts/beta_cd/README.md`
- `structures/hosts/sbe_beta_cd/README.md`

### Ligand preparation

Ligand preparation is documented in:

- `structures/curcumin/README.md`
- `structures/bdmc/README.md`

### Docking protocol

Docking was performed using **AutoDock Vina v1.2.3** on **Google Colab**.

For each system:

1. The receptor was loaded as a rigid PDBQT file.
2. The ligand was loaded as a flexible PDBQT file (with a torsion tree
   defining rotatable bonds).
3. The grid box was centered on the host cavity (see table above).
4. Vina was run with `exhaustiveness = 16` and `num_modes = 10`.
5. The best binding pose (Pose 1) was selected based on the lowest
   binding energy.
6. The pose was visually inspected in **UCSF ChimeraX** to confirm the
   ligand is located **inside** the host cavity (not floating outside).

### Notebooks

The Colab notebooks used for each docking system are available in
`notebooks/docking/`:

| Notebook | System |
|----------|--------|
| `docking_cur_bcd.ipynb` | Curcumin + β-CD |
| `docking_bdmc_bcd.ipynb` | BDMC + β-CD |
| `docking_cur_sbe_bcd.ipynb` | Curcumin + SBE-β-CD |
| `docking_bdmc_sbe_bcd.ipynb` | BDMC + SBE-β-CD |

## Interpretation

- **All four systems show spontaneous binding** (negative ΔG values),
  confirming that both curcuminoids form inclusion complexes with both
  cyclodextrin hosts.
- **β-CD is the stronger binder** for both guests, possibly because the
  charged sulfobutyl ether groups in SBE-β-CD interfere with the
  hydrophobic encapsulation of the neutral guests.
- **Curcumin binds more strongly than BDMC** in both hosts, suggesting
  that the methoxy (−OCH₃) groups contribute to favorable hydrophobic
  interactions within the cavity.
- The **grid box size** required for each host reflects the differing
  cavity accessibility: β-CD is best described by a 14 Å box, while
  the bulkier SBE-β-CD requires an 18 Å box to accommodate the
  flexible sulfobutyl ether chains.
- Docking scores are in the range **−4.8 to −5.4 kcal/mol**, consistent
  with reported values for 1:1 cyclodextrin–curcuminoid systems.

## Visualization in ChimeraX

To reproduce the visualizations:

```bash
# Curcumin + β-CD
open structures/hosts/beta_cd/bcd_minimized_byAutodock.pdbqt
open results/docking/cur_bcd_docked_14A.pdbqt
hide #1.2-#1.10

# BDMC + β-CD
open structures/hosts/beta_cd/bcd_minimized_byAutodock.pdbqt
open results/docking/bdmc14_bcd_docked.pdbqt
hide #1.2-#1.10

# Curcumin + SBE-β-CD
open structures/hosts/sbe_beta_cd/sbe_beta_cd_receptor.pdbqt
open results/docking/cur_sbe_docked.pdbqt
hide #1.2-#1.10

# BDMC + SBE-β-CD
open structures/hosts/sbe_beta_cd/sbe_beta_cd_receptor.pdbqt
open results/docking/bdmc_sbe_docked18.pdbqt
hide #1.2-#1.10