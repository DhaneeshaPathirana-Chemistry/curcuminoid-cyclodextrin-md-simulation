#!/usr/bin/env python3
"""
clean_receptor.py
=================

Remove ligand-style tags (ROOT, BRANCH, TORSDOF) from a PDBQT file so it
can be used as a rigid receptor in AutoDock Vina.

Background
----------
When a PDBQT file is created by OpenBabel, Avogadro, or Antechamber for a
small molecule (like a cyclodextrin), it is treated as a flexible ligand:
the file contains ROOT, BRANCH, and TORSDOF tags that describe which
bonds can rotate.

AutoDock Vina does not accept these tags in a receptor file. If they are
present, Vina raises:

    PDBQT parsing error: Unknown or inappropriate tag found in rigid
    receptor. > ROOT

This script removes ROOT, BRANCH, and TORSDOF lines, producing a clean
rigid-receptor PDBQT file that Vina can read.

Usage
-----
    python clean_receptor.py <input.pdbqt> <output.pdbqt>

Example
-------
    python clean_receptor.py sbe_beta_cd_raw.pdbqt sbe_beta_cd_receptor.pdbqt

Author
------
P. Dhaneesha Ranmini Pathirana
B.Sc. (Honours) in Chemistry, University of Peradeniya, Sri Lanka

Note
----
This script was developed as part of the research workflow for the
SBE-β-CD receptor preparation described in the project README. It
formalizes the file-transformation step applied to PDBQT files during
receptor preparation.

Part of the project:
    Comparative Inclusion Complexation of Curcumin and
    Bisdemethoxycurcumin with β-Cyclodextrin and Sulfobutyl Ether
    β-Cyclodextrin: A Molecular Docking and Molecular Dynamics Study
"""

import argparse
import os
import sys


# Tags that are valid in a ligand PDBQT file but NOT in a receptor file
LIGAND_TAGS = ("ROOT", "BRANCH", "TORSDOF")


def clean_receptor(input_path: str, output_path: str) -> None:
    """
    Remove ligand-style tags from a PDBQT file to produce a rigid receptor.

    Parameters
    ----------
    input_path : str
        Path to the input PDBQT file (may contain ROOT/BRANCH/TORSDOF).
    output_path : str
        Path to write the cleaned, receptor-only PDBQT file.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    ValueError
        If the input file contains no ATOM/HETATM lines after cleaning.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r") as f:
        lines = f.readlines()

    cleaned_lines = []
    removed_count = 0
    for line in lines:
        if any(tag in line for tag in LIGAND_TAGS):
            removed_count += 1
            continue
        cleaned_lines.append(line)

    atom_count = sum(
        1 for line in cleaned_lines
        if line.startswith(("ATOM", "HETATM"))
    )

    if atom_count == 0:
        raise ValueError(
            f"No ATOM/HETATM lines found in cleaned output. "
            f"Input file may be corrupted or empty: {input_path}"
        )

    with open(output_path, "w") as f:
        f.writelines(cleaned_lines)

    print(f"✅ Cleaned receptor written to: {output_path}")
    print(f"   Input file      : {input_path}")
    print(f"   Removed lines   : {removed_count} (ROOT / BRANCH / TORSDOF)")
    print(f"   Atoms in output : {atom_count}")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Remove ligand-style tags (ROOT, BRANCH, TORSDOF) from a PDBQT "
            "file to produce a rigid receptor for AutoDock Vina."
        ),
        epilog=(
            "Example:\n"
            "    python clean_receptor.py sbe_beta_cd_raw.pdbqt "
            "sbe_beta_cd_receptor.pdbqt"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input_pdbqt",
        help="Path to the input PDBQT file (with ROOT/BRANCH/TORSDOF tags).",
    )
    parser.add_argument(
        "output_pdbqt",
        help="Path to write the cleaned receptor PDBQT file.",
    )
    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_args()

    try:
        clean_receptor(args.input_pdbqt, args.output_pdbqt)
    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())