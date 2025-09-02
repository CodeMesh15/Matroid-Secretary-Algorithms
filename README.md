# Matroid Secretary Algorithms

Implementations and experiments for secretary algorithms under matroid constraints, including multiple-secretary variants and testers for graphic, transversal, and gammoid matroids.

## Features
- Baselines for classical and multiple-secretary settings (random-order arrivals).
- Independence oracles for graphic, transversal, and gammoid families.
- Reproducible sweeps across constrained regimes; CSV logging and plots.

## Getting Started
Prerequisites: Python 3.10+, pip, virtualenv

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```


## Quick Start

Synthetic graphic matroid instance, small-regime sweep
```python
python -m experiments.run --matroid graphic --n 200 --rank 40 --seeds 10
```
Transversal matroid via bipartite generator
```python
python -m experiments.run --matroid transversal --left 120 --right 80 --p 0.08 --seeds 10
```
Gammoid via random DAG with source/target sets
```python
python -m experiments.run --matroid gammoid --nodes 150 --p 0.03 --sources 10 --targets 30 --seeds 10
```


## Results and Logs
See `results/` for CSVs and `docs/` for literature notes and the constrained-regime improvement log.

## License
MIT (adjust as needed).

