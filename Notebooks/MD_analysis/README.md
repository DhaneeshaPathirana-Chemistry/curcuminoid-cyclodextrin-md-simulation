# Analysis — Post-Production MD Results

Analysis outputs for the 100 ns production MD trajectories of the
curcuminoid–cyclodextrin inclusion complexes.

Each system has its own folder containing the raw analysis data (`.xvg`)
and publication-ready plots (`plots/`). Cross-system summary tables live
in `tables/`. MM/PBSA binding free energies live in `mm_pbsa/`.

---

## 📊 Analysis types

| # | Analysis | File | Description |
|---|----------|------|-------------|
| 1 | RMSD — complex | `rmsd_complex.xvg` | Backbone RMSD of the entire complex vs. starting structure, after alignment |
| 2 | RMSD — host | `rmsd_host.xvg` | RMSD of the host (β-CD or SBE-β-CD) only |
| 3 | RMSD — guest | `rmsd_guest.xvg` | RMSD of the guest (curcumin or BDMC) only |
| 4 | Radius of gyration | `rg.xvg` | Compactness of the complex over time |
| 5 | COM distance | `com_distance.xvg` | Center-of-mass distance between host and guest — monitors binding stability |
| 6 | Hydrogen bonds | `hbonds.xvg` | Number of host–guest hydrogen bonds per frame |
| 7 | RMSF | `rmsf.xvg` | Per-atom (or per-residue) fluctuations — identifies flexible regions |
| 8 | SASA | `sasa.xvg` | Solvent-accessible surface area — estimates guest burial upon complexation |

All `.xvg` files are XVG-format GROMACS output; column 1 is time (ps),
column 2 (and beyond) is the analysis quantity.

---

## 🔬 Method summary

For each system, the PBC-corrected trajectory
(`results/md_simulations_100ns/<system>/step5_production_fixed.xtc`)
was analyzed with the corresponding topology
(`step5_production.tpr`) and index file (`index.ndx`).

**Preprocessing**
- Loaded trajectory and topology
- Aligned all frames to the first frame to remove overall rotation and
  translation (using the host as the reference group)

**Analysis tools**

| Analysis | GROMACS tool | Notes |
|----------|--------------|-------|
| RMSD | `gmx rms` | Separate runs for complex, host, and guest |
| Radius of gyration | `gmx gyrate` | On the full complex |
| COM distance | `gmx distance` | Host COM ↔ guest COM |
| Hydrogen bonds | `gmx hbond` | Host as donor/acceptor, guest as acceptor/donor |
| RMSF | `gmx rmsf` | Per-residue fluctuations |
| SASA | `gmx sasa` | On the full complex |

Full commands and parameter choices are documented in the analysis
notebook: `MD_Analysis_cur_bcd_afterPBC.ipynb`.

---

## 📓 Notebooks

| Notebook | System |
|----------|--------|
| `notebooks/analysis/MD_Analysis_cur_bcd_afterPBC.ipynb` | CUR + β-CD |

---

## 📁 Related documentation

- `notebooks/analysis/README.md` — analysis notebooks overview
- `results/md_simulations_100ns/README.md` — source trajectories
- `results/md_simulations_100ns/cur_bcd/README.md` — CUR + β-CD production MD
- `results/analysis/mm_pbsa/README.md` — MM/PBSA binding free energy
- `docs/methodology.md` — full methods writeup
- `docs/troubleshooting.md` — issues encountered during analysis