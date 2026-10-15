# CUR–BCD MD Analysis Results

Analysis outputs from a **100 ns Molecular Dynamics simulation** of a
**Curcumin (CUR) / β-Cyclodextrin (BCD)** inclusion complex.

This repository hosts the **figures and quantitative summaries** produced by
the analysis notebook. The notebook itself is included under `notebooks/`
for reproducibility.

---

##  Key Results

| Quantity | Value |
|---|---|
| **Complex RMSD** (mean ± SD) | **4.12 ± 1.90 Å** |
| Host (BCD) RMSD | 1.74 ± 0.15 Å |
| Guest (CUR) RMSD | 3.63 ± 0.61 Å |
| **Radius of gyration** (clean) | **6.25 ± 0.13 Å** |
| **Average H-bonds (BCD ↔ CUR)** | **2.88 ± 1.53** (max 10) |
| **COM distance** (median) | **2.01 Å** (95th pct = 4.33 Å) |
| **RMSF (BCD)** | 0.93 Å |
| **RMSF (CUR)** | 6.08 Å (after outlier removal) |
| **CUR SASA** (free → bound) | 381.8 → 223.7 Å² |
| **ΔSASA (buried)** | **158.1 Å²** |
| **Fraction of CUR buried** | **41.4 %** |

### Interpretation

-  **Stable complex** — BCD stays very rigid (RMSF 0.93 Å) and the complex
  RMSD stays within ~4 Å over 100 ns.
-  **CUR remains bound** — COM distance stays at ~2 Å (a true inclusion),
  with only brief excursions > 12 Å (< 0.5 % of frames).
-  **Persistent H-bonding** — an average of ~3 simultaneous H-bonds anchor
  CUR inside the BCD cavity.
-  **Strong burial** — ~41 % of the CUR solvent-accessible surface becomes
  buried upon binding.
- **Guest flexibility retained** — CUR keeps internal flexibility
  (RMSF ≈ 6 Å), typical of a guest inside a host cavity.

---

## Figures

All figures are in [`results/figures/`](results/figures/):

| Figure | Description |
|---|---|
| `rmsd_final.png` | RMSD of complex / host / guest |
| `rg_final.png` | Radius of gyration |
| `hbonds_final.png` | Hydrogen-bond count over time |
| `com_distance_final.png` | BCD–CUR center-of-mass distance |
| `rmsf_final.png` | Per-atom RMSF |
| `rmsf_cur_clean.png` | CUR RMSF with PBC artifacts removed |
| `sasa_analysis.png` | CUR SASA: free vs. complexed |

---

##  Summary Files

| File | Description |
|---|---|
| [`results/analysis_summary.txt`](results/analysis_summary.txt) | Human-readable summary |
| [`results/analysis_summary.json`](results/analysis_summary.json) | Machine-readable summary |

---

##  How the Results Were Produced

The analysis notebook
[`notebooks/CUR-BCD_100ns_MD_Analysis.ipynb`](notebooks/CUR-BCD_100ns_MD_Analysis.ipynb)
computes all of the above from the GROMACS trajectory. It performs:

1. **Trajectory loading & alignment** — aligns every frame onto the host (BCD)
2. **RMSD** — structural stability of host, guest, and complex
3. **Radius of Gyration** — compactness of the complex
4. **Center-of-Mass Distance** — host–guest proximity
5. **Hydrogen-Bond Analysis** — O···O contacts within 3.5 Å
6. **RMSF** — per-atom flexibility, with PBC-artifact frames excluded
7. **SASA** — custom golden-spiral SASA to estimate guest burial

The notebook is Colab-compatible:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DhaneeshaPathirana-Chemistry/curcuminoid-cyclodextrin-md-simulation/blob/main/notebooks/CUR-BCD_100ns_MD_Analysis.ipynb)

---

##  License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE).

---

## Author

**Dhaneesha Pathirana**

---

## Acknowledgements

- [MDAnalysis](https://www.mdanalysis.org/) — trajectory analysis
- [GROMACS](https://www.gromacs.org/) — MD engine that produced the trajectory
- [Google Colab](https://colab.research.google.com/) — execution environment
