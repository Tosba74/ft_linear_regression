import sys


class CarPriceEstimator:
    def __init__(self, theta0: float, theta1: float):
        self.theta0 = theta0
        self.theta1 = theta1

    def estimate_price(self, mileage: float) -> float:
        """Estimate the price of a car based on its mileage.
        theta0 + (theta1 * kilometrage)
        """
        return self.theta0 + (self.theta1 * mileage)

    def header(self):
        print("*--------------------------------------------------*")
        print("| Estimate the price of a car based on its mileage |")
        print("*--------------------------------------------------*")

    def get_mileage(self) -> float:
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
    theta0 = 0
    theta1 = 0
    estimator = CarPriceEstimator(theta0, theta1)
    mileage = estimator.get_mileage()
    price = estimator.estimate_price(mileage)
    print(f"Estimated price for a car with {mileage} km: {price:.2f} €")


if __name__ == "__main__":
    main()
