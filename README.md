# Comparative Inclusion Complexation of Curcumin with β-Cyclodextrin and Sulfobutyl Ether β-Cyclodextrin

## Project Overview

This computational chemistry project investigates the inclusion complexation of **curcumin (CUR)** with two cyclodextrin-based host molecules:

* **β-cyclodextrin (β-CD)**
* **Sulfobutyl ether β-cyclodextrin (SBE-β-CD)**

Molecular docking and molecular dynamics (MD) simulations are being used to investigate the interactions, binding orientations, and structural behavior of curcumin within the two host molecules.

The study focuses on a comparative computational analysis of:

* **β-CD–Curcumin**
* **SBE-β-CD–Curcumin**

---

## Research Objective

The primary objective of this study is to investigate and compare the molecular interactions and stability of curcumin inclusion complexes formed with β-CD and SBE-β-CD.

The study aims to explore:

1. The preferred orientation of curcumin within the cyclodextrin cavities.
2. The interactions between curcumin and the cyclodextrin host molecules.
3. The structural stability of the inclusion complexes during molecular dynamics simulations.
4. Differences in the behavior of curcumin when complexed with β-CD and SBE-β-CD.
5. The influence of the sulfobutyl ether modification on the interaction and stability of the curcumin complex.

---

## Computational Systems

| Host     | Guest    | Molecular Docking | Molecular Dynamics |
| -------- | -------- | ----------------- | ------------------ |
| β-CD     | Curcumin | Completed         | Completed          |
| SBE-β-CD | Curcumin | Completed         | In progress        |

---

## Computational Workflow

The computational workflow consists of the following stages:

**Molecular structure preparation → Molecular docking → Selection and preparation of docked complex → GROMACS system preparation → Energy minimization and equilibration → Molecular dynamics simulation → Trajectory processing → Trajectory analysis → Comparative analysis**

Molecular docking has been completed for both host–guest systems.

Molecular dynamics simulation has been completed for the **β-CD–Curcumin** complex. The MD workflow is currently being extended to the **SBE-β-CD–Curcumin** complex.

---

## Molecular Structure Preparation

The molecular structures of the host and guest molecules were prepared and inspected using molecular modelling and visualization tools.

### Host molecules

* β-cyclodextrin (β-CD)
* Sulfobutyl ether β-cyclodextrin (SBE-β-CD)

### Guest molecule

* Curcumin (CUR)

Structure preparation and inspection involved **Avogadro** and **UCSF ChimeraX**.

Energy minimization and preparation of the molecules for docking were carried out using **AutoDock Tools** and **PyRx**, as applicable to the individual molecular systems.

The detailed preparation steps are documented in the corresponding notebooks and workflow files.

---

## Molecular Docking

Molecular docking was performed for both host–guest systems using **AutoDock Vina**.

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

The β-CD–Curcumin MD simulation has been completed.

Final trajectory-analysis results and figures will be added following completion of the analysis.

The SBE-β-CD–Curcumin MD simulation and subsequent comparative analysis are currently in progress.

---

## Repository Structure

```text
.
├── README.md
│
├── structures/
│   ├── hosts/
│   │   ├── beta_cd/
│   │   └── sbe_beta_cd/
│   └── curcumin/
│
├── notebooks/
│   ├── docking/
│   ├── molecular_dynamics/
│   └── analysis/
│
├── scripts/
│   ├── docking/
│   ├── molecular_dynamics/
│   └── analysis/
│
├── results/
│   ├── docking/
│   ├── molecular_dynamics/
│   ├── figures/
│   └── tables/
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
* **AutoDock Vina** — molecular docking
* **CHARMM-GUI** — preparation of GROMACS input files
* **GROMACS** — molecular dynamics simulations and trajectory processing
* **VMD** — molecular dynamics trajectory visualization
* **Python** — data processing and analysis
* **Google Colab** — computational notebooks and molecular dynamics workflow
* **MobaXterm** — terminal-based computational workflow

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
docs/troubleshooting.md
```

This documentation will focus on significant issues that are relevant to understanding or reproducing the computational workflow, including topology and residue-naming issues encountered during preparation of the β-CD–Curcumin system.

---

## Project Status

**Ongoing**

### Completed

* [x] Preparation of β-CD structure
* [x] Preparation of SBE-β-CD structure
* [x] Preparation of curcumin structure
* [x] β-CD–Curcumin molecular docking
* [x] SBE-β-CD–Curcumin molecular docking
* [x] Selection and preparation of β-CD–Curcumin docked complex
* [x] β-CD–Curcumin GROMACS system preparation
* [x] β-CD–Curcumin molecular dynamics simulation

### In Progress

* [ ] β-CD–Curcumin trajectory analysis
* [ ] SBE-β-CD–Curcumin molecular dynamics simulation
* [ ] SBE-β-CD–Curcumin trajectory analysis
* [ ] Comparative analysis of the two complexes
* [ ] Final figures and tables
* [ ] Final interpretation of results

---

## Author

**P. Dhaneesha Ranmini Pathirana**

B.Sc. (Honours) in Chemistry
University of Peradeniya, Sri Lanka

---

## Project Note

This repository documents an ongoing computational chemistry study of curcumin inclusion complexes with β-cyclodextrin and sulfobutyl ether β-cyclodextrin using molecular docking and molecular dynamics simulations.
