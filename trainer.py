import sys
import pandas as pd
from pathlib import Path

class Trainer:
    def __init__(self):
        self.datapath = ""
        self.dataset = None
        self.theta0 = 0.0
        self.theta1 = 0.0
        pass

    def print_results(self):
        """ Print the values of theta0 and theta1."""
        print(f"New car price (theta0): {self.theta0}")
        print(f"Mileage discount (theta1): {self.theta1}")

    def output_thetas(self, filename='theta.txt'):
        """ Save theta0 and theta1 to a file."""
        with open(filename, 'w') as f:
            f.write(f"{self.theta0}\n")
            f.write(f"{self.theta1}\n")

    def check_datapath(self, csv_path: str):
        """ Check if the provided path is valid and points to a CSV file."""
        path = Path(csv_path)
        if not path.exists():
            print(f"Erreur: {csv_path}: Invalid file")
            sys.exit(1)
        if not path.suffix == '.csv':
            print(f"Erreur: {csv_path}: Not a CSV file")
            sys.exit(1)
        self.datapath = path

    def load_data(self, path: str):
        """ Load dataset from the provided CSV file path."""
        self.check_datapath(path)
        self.dataset = pd.read_csv(self.datapath)

    def training(self, path: str):
        """ Training the model to find theta0 and theta1."""
        self.header()
        self.load_data(path)
        self.theta0 = 15000.50  # Dummy value
        self.theta1 = -0.08500  # Dummy value
        print("Training completed.")
        self.print_results()
        self.output_thetas()

    def header(self):
        """ Prints the header."""
        print("*--------------------------------------------------*")
        print("| Training...                                      |")
        print("*--------------------------------------------------*")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python trainer.py <path/to/file.csv>")
        sys.exit(1)
    t = Trainer()
    t.training(sys.argv[1])