# Van der Waals with conserved charges
Framework to estimate van der Waals equation of state parameters for nuclear matter with a dependency on conserved charges (baryon number $B$, strangeness $S$, and electric charge $Q$)

[![License: GPL v3](https://img.shields.io/badge/License-University_of_Illinois/NCSA_Open_Source-blue.svg)](LICENSE)

## Overview
This is a framework to calculate the Hadron Resonance Gas (HRG) susceptibilities using a van der Waals equation of state with varying parameters dependent on conserved charges (baryon number $B$, strangeness $S$, and electric charge $Q$) as implemented in to execute [`Thermal-FIST`](https://github.com/vlvovch/Thermal-FIST).

## Features
- Generation of vdW EoS interaction parameters with different charge dependence prescriptions
- Full integration with [`Thermal-FIST`](https://github.com/vlvovch/Thermal-FIST)
- Efficient output in HDF5 format

## Installation
To install prerequisites, while on the main project directory, execute
```terminal
pip install -r requirements.txt
```

## Usage
To generate vdW EoS interaction parameters according to a specified prescription,
```terminal
python
```

To launch [`Thermal-FIST`](https://github.com/vlvovch/Thermal-FIST) and iterate over all possible interaction parameters,
```terminal
python src/cli.py
```

## Citation
If you use this code, please cite:
```bibtex
@misc{identifier,
      title={}, 
      author={Jordi Salinas San Martín and Feyisola Nana and Jacquelyn Noronha-Hostler},
      year={2025},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={nucl-th},
      url={https://arxiv.org/abs/}, 
}
```

## Contributing


## Authorship