import math
import random

def price_european_call(S0, K, T, r, sigma, num_paths):
    """
    Prices a European Call option using Monte Carlo simulation in pure Python.
    
    Parameters:
    S0: Initial stock price
    K: Strike price
    T: Time to maturity (years)
    r: Risk-free interest rate
    sigma: Volatility
    num_paths: Number of simulation paths
    """
    sum_payoffs = 0.0
    
    # Precompute constants
    drift = (r - 0.5 * sigma**2) * T
    vol = sigma * math.sqrt(T)
    
    for _ in range(num_paths):
        # Generate standard normal random variable using Box-Muller or random.gauss
        z = random.gauss(0.0, 1.0)
        
        # Simulate end stock price
        ST = S0 * math.exp(drift + vol * z)
        
        # Calculate payoff
        payoff = max(ST - K, 0.0)
        sum_payoffs += payoff
        
    # Average payoff discounted back to present value
    option_price = math.exp(-r * T) * (sum_payoffs / num_paths)
    return option_price

if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2
    paths = 1_000_000
    price = price_european_call(S0, K, T, r, sigma, paths)
    print(f"Baseline Pure Python Price: {price:.4f}")
