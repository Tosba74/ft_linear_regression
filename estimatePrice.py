def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    """Estimate the price of a car based on its mileage.
    Args:
        mileage (float): Car's mileage
        theta0 (float): theta0
        theta1 (float): theta1
    Returns:
        float: theta0 + (theta1 * kilometrage)
    """
    theta0 = 0
    theta1 = 0
    return theta0 + (theta1 * mileage)
