import sys
import pandas as pd
from pathlib import Path


def load_dataset(csv_path: str) -> pd.DataFrame:
    """Loading dataset from a file CSV.
    Take file path as argument and return a pandas DataFrame.
    """
    path = Path(csv_path)
    if not path.exists():
        print(f"Erreur: {csv_path}: Invalid file")
        sys.exit(1)
    if not path.suffix == '.csv':
        print(f"Erreur: {csv_path}: Not a CSV file")
        sys.exit(1)
    return pd.read_csv(path)


def print_dataset(dataset: pd.DataFrame):
    print(dataset.info())
    print(dataset.describe())
    # print(dataset)
