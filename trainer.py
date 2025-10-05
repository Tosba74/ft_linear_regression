import os
import sys
import csv
import pandas as pd


class Trainer:
    def __init__(self):
        self.datapath = ""
        self.dataset = {
            'km': [],
            'price': []
        }
        self.theta0 = 0.0
        self.theta1 = 0.0
        pass

    def check_datapath(self, csv_path: str):
        """ Check if the provided path is valid and points to a CSV file."""
        if not os.path.exists(csv_path):
            print(f"Erreur: {csv_path}: File not found")
            sys.exit(1)
    
        if not csv_path.lower().endswith('.csv'):
            print(f"Erreur: {csv_path}: Not a CSV file")
            sys.exit(1)
    
        self.datapath = csv_path

    def load_data(self, path: str):
        """ Load dataset from the provided CSV file path."""
        self.check_datapath(path)
        try:
            with open(self.datapath, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.dataset['km'].append(float(row['km']))
                    self.dataset['price'].append(float(row['price']))
        except IsADirectoryError:
            print(f"Erreur: {path}: Is a directory, not a file")
            sys.exit(1)
        except PermissionError:
            print(f"Erreur: {path}: Permission denied")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Erreur: {path}: Invalid file encoding")
            sys.exit(1)
        except csv.Error as e:
            print(f"Erreur: {path}: Invalid CSV format - {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            sys.exit(1)

    
    def print_results(self):
        """ Print the values of theta0 and theta1."""
        print(f"New car price (theta0): {self.theta0}")
        print(f"Mileage discount (theta1): {self.theta1}")

    def output_thetas(self, filename='theta.txt'):
        """ Save theta0 and theta1 to a file."""
        with open(filename, 'w') as f:
            f.write(f"{self.theta0}\n")
            f.write(f"{self.theta1}\n")

    def training(self, path: str):
        """ Training the model to find theta0 and theta1."""
        self.header()
        self.load_data(path)
        self.theta0 = 30000
        self.theta1 = -0.0500
        print("Training completed.")
        self.print_results()
        self.output_thetas()
        confirm = input("Are you sure to continue? (y/n): ")
        if confirm.lower() in ['y', 'yes']:
            print(self.dataset)
        
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