import sys
import pandas as pd
from pathlib import Path


def load_dataset(csv_path: str) -> pd.DataFrame:
    """Charge un dataset depuis un fichier CSV.
    Args:
        csv_path (str): Chemin vers le fichier CSV
    Returns:
        pd.DataFrame: Le dataset chargé
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
