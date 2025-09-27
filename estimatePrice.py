import sys


class CarPriceEstimator:
    def __init__(self, theta0: float = 0.0, theta1: float = 0.0):
        self.theta0 = theta0
        self.theta1 = theta1

    def estimate_price(self, mileage: float) -> float:
        """Estimate the price of a car based on its mileage.
        theta0 + (theta1 * kilometrage)
        """
        return self.theta0 + (self.theta1 * mileage)

    def load_thetas(self, filename='theta.txt'):
        """ Load theta0 and theta1 from a file."""
        with open(filename, 'r') as f:
            lines = f.readlines()
            self.theta0 = float(lines[0].strip())
            self.theta1 = float(lines[1].strip())

    def header(self):
        """ Prints the header."""
        print("*--------------------------------------------------*")
        print("| Estimate the price of a car based on its mileage |")
        print("*--------------------------------------------------*")

    def get_mileage(self) -> float:
        """ Prompts the user to enter the mileage and validates the input."""
        self.header()
        while True:
            try:
                mileage = float(input("Enter the car's mileage: "))
                if mileage < 0:
                    print("Mileage cannot be negative. Try again.")
                    continue
                if mileage > 1000000:
                    print("Wow! It's lot of mileage for a car.")
                    confirm = input("Are you sure to continue? (y/n): ")
                    if confirm.lower() in ['n', 'no']:
                        continue
                return mileage
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit(0)


def main():
    estimator = CarPriceEstimator()
    estimator.load_thetas()
    mileage = estimator.get_mileage()
    price = estimator.estimate_price(mileage)
    if price < 0:
        price = 0
    print(f"Estimated price for a car with {mileage} km: {price:.2f} €")


if __name__ == "__main__":
    main()
