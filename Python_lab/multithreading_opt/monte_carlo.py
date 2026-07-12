import math
import random
import os
import concurrent.futures

def simulate_paths(S0, K, drift, vol, num_paths):
    """Worker function for simulating a subset of paths."""
    sum_payoffs = 0.0
    for _ in range(num_paths):
        z = random.gauss(0.0, 1.0)
        ST = S0 * math.exp(drift + vol * z)
        payoff = ST - K
        if payoff > 0:
            sum_payoffs += payoff
    return sum_payoffs

def price_european_call(S0, K, T, r, sigma, num_paths):
    """
    Prices a European Call using Multithreading.
    Note: Python's GIL will limit the performance gain for CPU-bound tasks like this.
    """
    cores = os.cpu_count() or 1
    paths_per_core = num_paths // cores
    chunks = [paths_per_core] * cores
    chunks[0] += num_paths % cores
    
    drift = (r - 0.5 * sigma**2) * T
    vol = sigma * math.sqrt(T)
    
    total_payoff = 0.0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as executor:
        futures = [
            executor.submit(simulate_paths, S0, K, drift, vol, chunk) 
            for chunk in chunks
        ]
        
        for future in concurrent.futures.as_completed(futures):
            total_payoff += future.result()
            
    option_price = math.exp(-r * T) * (total_payoff / num_paths)
    return option_price

if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2
    paths = 1_000_000
    price = price_european_call(S0, K, T, r, sigma, paths)
    print(f"Multithreading Price: {price:.4f}")
