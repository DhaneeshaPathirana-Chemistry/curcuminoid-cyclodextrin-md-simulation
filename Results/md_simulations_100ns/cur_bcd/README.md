# CUR + β-CD — 100 ns Production MD

Production molecular dynamics outputs for the **curcumin + β-cyclodextrin**
inclusion complex (CUR + β-CD).

This folder is part of `results/md_simulations_100ns/`

---

## 📋 System summary

| Parameter | Value |
|-----------|-------|
| System | Curcumin (CUR) + β-cyclodextrin (β-CD) |
| Type | Host–guest inclusion complex |
| Force field | CHARMM36m |
| Water model | TIP3P |
| Salt | 0.15 M NaCl |
| Temperature | 298 K |
| Pressure | 1 bar |
| Simulation length | 100 ns |
| Timestep | 2 fs |
| Frames saved | 1000 (every 100 ps) |
| Engine | GROMACS 2023.3 |
| GPU | NVIDIA A100 (Google Colab) |
| Performance | ~1300 ns/day |
| Wall time | ~1 h 50 min |

---

## 📂 Files in this folder

| File | Size | Description |
|------|------|-------------|
| `step5_production.xtc` | ~13–15 MB | Raw production trajectory (100 ns, 1000 frames) |
| `step5_production_fixed.xtc` | ~13–15 MB | **PBC-corrected trajectory** — used for all analysis |
| `step5_production.gro` | < 1 MB | Final-frame coordinates |
| `step5_production.edr` | 1–5 MB | Energy time series (potential, kinetic, temperature, pressure) |
| `step5_production.tpr` | 1–5 MB | Compiled run input (topology + parameters) |
| `step5_production.log` | < 1 MB | GROMACS run log |
| `index.ndx` | < 100 KB | Index groups (from Stage 1) |

> **Note:** Both `step5_production.xtc` (raw) and `step5_production_fixed.xtc`
> (PBC-corrected) are kept for provenance. All analysis uses the `_fixed`
> version.

---

## 🔧 PBC correction (post-processing)

The raw trajectory was corrected for periodic boundary conditions **before
analysis**, so that the complex remains whole and centered across all
frames.

**Command used** (run in MobaXterm / WSL Ubuntu):

```bash
gmx trjconv -s step5_production.tpr \
    -f step5_production.xtc \
    -o step5_production_fixed.xtc \
    -pbc mol -center