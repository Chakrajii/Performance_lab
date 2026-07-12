import cProfile
import pstats
import sys
import os

# Add parent dir to sys.path to import baseline and others
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baseline.monte_carlo import price_european_call

if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2
    paths = 1_000_000
    
    print("Profiling Baseline Pure Python Implementation...")
    profiler = cProfile.Profile()
    profiler.enable()
    price = price_european_call(S0, K, T, r, sigma, paths)
    profiler.disable()
    
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats(10)
    print(f"Calculated Price: {price:.4f}")
