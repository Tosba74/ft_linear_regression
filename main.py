import sys
from estimatePrice import estimate_price
from trainer import trainer


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path/to/file.csv>")
        sys.exit(1)
    input_km = input("Enter the car's mileage : ")
    trainer(sys.argv[1])
    theta0 = 0
    theta1 = 0
    price = estimate_price(float(input_km), float(theta0), float(theta1))
    print(f"Estimated price for a car with {input_km} km : {price:.2f} €")


if __name__ == "__main__":
    main()
