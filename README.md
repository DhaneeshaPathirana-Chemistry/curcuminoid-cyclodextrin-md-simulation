# Comparative Inclusion Complexation of Curcumin and Bisdemethoxycurcumin with β-Cyclodextrin and Sulfobutyl Ether β-Cyclodextrin

## Project Overview

This computational chemistry project investigates the inclusion complexation of
two naturally occurring **curcuminoids** with two cyclodextrin-based host
molecules:

**Guests**
- **Curcumin (CUR)**
- **Bisdemethoxycurcumin (BDMC)**

**Hosts**
- **β-cyclodextrin (β-CD)**
- **Sulfobutyl ether β-cyclodextrin (SBE-β-CD)**

Molecular docking and molecular dynamics (MD) simulations are being used to investigate the interactions, binding orientations, and structural behavior of curcumin within the two host molecules.

| # | System | Short name |
|---|--------|------------|
| 1 | Curcumin + β-CD | `cur_bcd` |
| 2 | Curcumin + SBE-β-CD | `cur_sbe_bcd` |
| 3 | Bisdemethoxycurcumin + β-CD | `bdmc_bcd` |
| 4 | Bisdemethoxycurcumin + SBE-β-CD | `bdmc_sbe_bcd` |

The comparison focuses on:

- Preferred binding orientations of each curcuminoid inside each host cavity
- Non-covalent interactions (hydrogen bonds, van der Waals contacts)
- Structural stability of each inclusion complex over 100 ns
- Effect of the sulfobutyl ether modification on binding and stability
- Comparative behavior of curcumin vs. bisdemethoxycurcumin
  
---

## Research Objective

1. Identify the preferred orientation of CUR and BDMC within the β-CD and
   SBE-β-CD cavities.
2. Characterize host–guest interactions stabilizing each inclusion complex.
3. Assess the structural stability of each complex during 100 ns MD.
4. Compare CUR vs. BDMC behavior in each host.
5. Compare β-CD vs. SBE-β-CD behavior for each guest.
6. Evaluate the influence of the sulfobutyl ether modification on complexation.

---

## Computational Systems

| Host | Guest | Docking | MD (100 ns) | Analysis |
|------|-------|---------|-------------|----------|
| β-CD | Curcumin | ✅ Completed | ✅ Completed | 🔄 In progress |
| SBE-β-CD | Curcumin | ✅ Completed | 🔄 In progress | ⏳ Pending |
| β-CD | BDMC | ✅ Completed | ⏳ Pending | ⏳ Pending |
| SBE-β-CD | BDMC | ✅ Completed | ⏳ Pending | ⏳ Pending |

---

## Computational Workflow

The computational workflow consists of the following stages:

```
Structure preparation
      ↓
Molecular docking (AutoDock Vina)
      ↓
Selection and preparation of the docked complex (UCSF ChimeraX + DockPrep)
      ↓
GROMACS system preparation (CHARMM-GUI)
      ↓
Energy minimization + equilibration (GROMACS via MobaXterm)
      ↓
Production MD — 100 ns (GROMACS via Google Colab / GPU)
      ↓
Trajectory post-processing — PBC correction (GROMACS via MobaXterm)
      ↓
Visualization (VMD) + Trajectory analysis (Python / Colab)
      ↓
Binding free energy (gmx_MMPBSA)
      ↓
Comparative analysis across all four systems

```

Molecular docking has been completed for all host–guest systems.

Molecular dynamics simulation has been completed for the **β-CD–Curcumin** complex. The MD workflow is currently being extended to the **SBE-β-CD–Curcumin** complex.

---

## Molecular Structure Preparation

The molecular structures of the host and guest molecules were prepared and inspected using molecular modelling and visualization tools.

### Host molecules

* β-cyclodextrin (β-CD)
* Sulfobutyl ether β-cyclodextrin (SBE-β-CD)

### Guest molecule

* Curcumin (CUR)
* Bisdemethoxycurcumin (BDMC)

Structure preparation and inspection involved **Avogadro2** and **UCSF ChimeraX version: 1.6.1**.

Energy minimization and preparation of the molecules for docking were carried out using **AutoDock Tools 1.5.7** and **PyRx**, as applicable to the individual molecular systems.

The detailed preparation steps are documented in the corresponding notebooks and workflow files.

---

## Molecular Docking

Molecular docking was performed for both host–guest systems using **AutoDock Vina v1.2.3**.

### β-CD–Curcumin

Docking was used to investigate possible orientations of curcumin within the β-CD cavity and to identify suitable binding poses for subsequent molecular dynamics simulation.

AutoDock Vina was installed and used in **Google Colab** for the docking calculations.

### SBE-β-CD–Curcumin

Docking was performed to investigate the interaction of curcumin with the modified cyclodextrin host and to identify suitable poses for further computational analysis.

AutoDock Vina was used in **Google Colab** for the docking calculations.

The docking input structures, configuration files, output files, and selected docking results are organized within the repository.

---

## Selection and Preparation of the Docked Complex

Following molecular docking, a suitable docked pose was selected for further molecular dynamics simulations.

The selected complex was inspected and prepared using **UCSF ChimeraX with DockPrep**.

During preparation of the β-CD–Curcumin system, topology-related issues were encountered. These were addressed by checking and adjusting residue names to ensure compatibility with the molecular dynamics setup.

Important troubleshooting steps are documented separately in the repository.

---

## Preparation of GROMACS Input Files

### β-CD–Curcumin

The GROMACS input files required for the molecular dynamics workflow were generated using **CHARMM-GUI**.

The resulting system files were subsequently used for system preparation, equilibration, and molecular dynamics simulations.

---

## Energy Minimization and Equilibration

### β-CD–Curcumin

Energy minimization and equilibration of the prepared system were carried out using **GROMACS** through a terminal environment accessed using **MobaXterm**.

These stages were performed to prepare the system for the production molecular dynamics simulation.

---

## Molecular Dynamics Simulations

Molecular dynamics simulations are being performed using **GROMACS** to investigate the behavior of the docked inclusion complexes over time.

### β-CD–Curcumin

The molecular dynamics simulation has been completed for the β-CD–Curcumin complex.

The resulting trajectory is being processed and analyzed to investigate the structural behavior and stability of the inclusion complex.

### SBE-β-CD–Curcumin

The SBE-β-CD–Curcumin docking calculation has been completed. Molecular dynamics simulation is the next stage of the computational workflow and is currently in progress.

---

## Trajectory Processing and Periodic Boundary Conditions

### β-CD–Curcumin

Trajectory processing, including treatment of periodic boundary conditions, was carried out using **GROMACS/MobaXterm** as part of the trajectory preparation workflow.

The processed trajectory was subsequently visualized using **VMD** for inspection of the molecular dynamics simulation.

Relevant trajectory-processing scripts and files will be included in the repository where appropriate.

---

## Trajectory Analysis

### β-CD–Curcumin

The molecular dynamics trajectory is being analyzed to characterize the structural behavior of the host–guest complex.

Depending on the finalized analysis, relevant parameters may include:

* Root-mean-square deviation (RMSD)
* Root-mean-square fluctuation (RMSF)
* Radius of gyration
* Host–guest distance
* Hydrogen-bond interactions
* Host–guest contacts
* Other relevant structural or interaction parameters

The final analysis methods, parameters, and scripts will be documented in the corresponding notebooks and analysis files.

---

## Results

### Molecular Docking

Docking calculations have been completed for both:

* β-CD–Curcumin
* SBE-β-CD–Curcumin

Final docking scores, selected poses, interaction analyses, and visualization figures will be added here once the results have been finalized.

### Molecular Dynamics

The β-CD–Curcumin 100ns MD simulation has been completed.

Final trajectory-analysis results and figures will be added following completion of the analysis.

The SBE-β-CD–Curcumin MD simulation and subsequent comparative analysis are currently in progress.

---

## Repository Structure

```text
.
curcuminoid-cyclodextrin-md-simulation/
│
├── README.md
│
├── structures/                              # Input structures
│   ├── hosts/
│   │   ├── beta_cd/
│   │   └── sbe_beta_cd/
│   └── guests/
│       ├── curcumin/
│       └── bdmc/
│
├── notebooks/                               # Interactive workflows
│   ├── docking/                             # 4 docking notebooks
│   ├── md_analysis/                         # CUR + β-CD analysis notebook
│   └── md_simulations_100ns/                # MD workflow notebooks
│       └── bcd_cur/
│
├── scripts/                                 # Reusable scripts
│   └── docking/
│       └── clean_receptor.py
│
├── results/                                 # Outputs (per stage)
│   ├── docking/                             # AutoDock Vina outputs + logs
│   ├── best_poses/                          # Best pose per system (4 × .pdb)
│   ├── md_simulations_100ns/                # Production MD outputs
│   │   └── cur_bcd/
│   │       ├── bcd_only_MD_result/
│   │       ├── cur_bcd_MD_result/
│   │       └── cur_only_MD_result/
│   ├── md_analysis/                         # Trajectory analysis outputs
│   │   └── bcd_cur/                         # plots + summaries
│   └── visualization/                       # VMD render
│       └── cur_bcd_complex.png
│
└── docs/
    └── troubleshooting.md
```

---

## Software and Computational Tools

The project uses a combination of molecular modelling, docking, molecular dynamics, visualization, and data-analysis tools:

* **Avogadro** — molecular structure preparation and visualization
* **UCSF ChimeraX** — molecular structure inspection and DockPrep
* **AutoDock Tools** — molecular preparation for docking
* **PyRx** — molecular preparation and docking workflow
* **AutoDock Vina v1.2.3** — molecular docking
* **CHARMM-GUI** — preparation of GROMACS input files
* **GROMACS 2023.3** — molecular dynamics simulations and trajectory processing
* **VMD 2.0.0a6** — molecular dynamics trajectory visualization
* **Python 3.10+** — data processing and analysis
* **Google Colab** — computational notebooks and molecular dynamics workflow
* **MobaXterm (WSL Ubuntu 24.04)** — terminal-based computational workflow

Software versions and relevant computational parameters will be documented in the corresponding workflow files where applicable.

---

## Reproducibility

This repository is intended to document the computational workflow used in this study.

Where applicable, the repository includes:

* Molecular structures used as computational inputs
* Docking configuration files
* Docking output files
* Molecular dynamics input files
* Shell/terminal scripts
* Python analysis scripts
* Google Colab/Jupyter notebooks
* Selected results and figures
* Documentation of important computational steps
* Troubleshooting information for significant computational issues

Large raw simulation trajectories and unnecessary intermediate files may be excluded because of their size.

---

## Troubleshooting

Important computational issues encountered during development of the workflow will be documented in:

```text
docs/troubleshooting_cur_bcd.md
```

This documentation will focus on significant issues that are relevant to understanding or reproducing the computational workflow, including topology and residue-naming issues encountered during preparation of the β-CD–Curcumin system.

---

## Project Status

**Ongoing**

### Completed


* ☑ Molecular docking — all four systems
* ☑ Best-pose extraction and complex building — all four systems
* ☑ GROMACS system preparation — CUR + β-CD
* ☑ Energy minimization + equilibration — CUR + β-CD
* ☑ 100 ns production MD — CUR + β-CD
* ☑ PBC correction + trajectory analysis — CUR + β-CD


### In Progress

* 🔄 MM-PBSA analysis - CUR + β-CD
* 🔄 100 ns production MD — CUR + SBE-β-CD

### Planned

* □ GROMACS system preparation + MD — BDMC + β-CD
* □ GROMACS system preparation + MD — BDMC + SBE-β-CD
* □ Trajectory analysis — remaining three systems
* □ Comparative analysis across all four systems
* □ Final figures and summary tables

---

## Author

**P. Dhaneesha Ranmini Pathirana**

B.Sc. (Honours) in Chemistry
University of Peradeniya, Sri Lanka

---

## Project Note

This repository documents an ongoing computational study comparing the
inclusion complexation of curcumin and bisdemethoxycurcumin with
β-cyclodextrin and sulfobutyl ether β-cyclodextrin, using molecular docking
and 100 ns molecular dynamics simulations. Documentation is updated as the
workflow progresses. 
