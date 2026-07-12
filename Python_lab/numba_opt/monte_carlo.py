import math
import random
from numba import njit

@njit
def price_european_call_numba(S0, K, T, r, sigma, num_paths):
    """
    Prices a European Call option using Numba JIT compilation.
    Numba excels at optimizing tight loops, so we use the pure Python logic here.
    """
    sum_payoffs = 0.0
    
    drift = (r - 0.5 * sigma**2) * T
    vol = sigma * math.sqrt(T)
    
    for _ in range(num_paths):
        z = random.gauss(0.0, 1.0)
        ST = S0 * math.exp(drift + vol * z)
        payoff = ST - K
        if payoff > 0:
            sum_payoffs += payoff
            
    option_price = math.exp(-r * T) * (sum_payoffs / num_paths)
    return option_price

def price_european_call(S0, K, T, r, sigma, num_paths):
    return price_european_call_numba(S0, K, T, r, sigma, num_paths)

if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2
    paths = 1_000_000
    
    # Warm-up run to trigger compilation
    _ = price_european_call(S0, K, T, r, sigma, 10)
    
    price = price_european_call(S0, K, T, r, sigma, paths)
    print(f"Numba JIT Price: {price:.4f}")
