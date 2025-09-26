class CarPriceEstimator:
    def __init__(self, theta0: float, theta1: float):
        self.theta0 = theta0
        self.theta1 = theta1

    def estimate_price(self, mileage: float) -> float:
        """Estimate the price of a car based on its mileage.
        theta0 + (theta1 * kilometrage)
        """
        return self.theta0 + (self.theta1 * mileage)


def main():
    theta0 = 0
    theta1 = 0
    estimator = CarPriceEstimator(theta0, theta1)
    mileage = float(input("Enter the car's mileage: "))
    price = estimator.estimate_price(mileage)
    print(f"Estimated price for a car with {mileage} km: {price:.2f} €")


if __name__ == "__main__":
    main()
