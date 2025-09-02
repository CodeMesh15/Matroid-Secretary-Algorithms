import argparse, random, pandas as pd, numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--matroid", choices=["graphic","transversal","gammoid"], required=True)
    parser.add_argument("--n", type=int, default=200)
    parser.add_argument("--rank", type=int, default=40)
    parser.add_argument("--seeds", type=int, default=5)
    args = parser.parse_args()
    # TODO: generate instance by matroid type, sample random weights and arrivals,
    # run algorithms, log CSV to results/
    print("Run placeholder; fill with generators and loggers.")

if __name__ == "__main__":
    main()
