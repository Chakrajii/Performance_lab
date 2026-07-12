import numpy as np

def price_european_call(S0, K, T, r, sigma, num_paths):
    """
    Prices a European Call option using Monte Carlo simulation with NumPy vectorization.
    """
    # Generate array of standard normal random variables
    z = np.random.standard_normal(num_paths)
    
    # Simulate end stock prices (vectorized)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)
    
    # Calculate payoffs (vectorized)
    payoffs = np.maximum(ST - K, 0.0)
    
    # Average payoff discounted to present value
    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price

if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2
    paths = 1_000_000
    price = price_european_call(S0, K, T, r, sigma, paths)
    print(f"NumPy Vectorized Price: {price:.4f}")
