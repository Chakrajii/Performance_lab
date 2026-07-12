import time
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baseline.monte_carlo import price_european_call as baseline_call
from numpy_opt.monte_carlo import price_european_call as numpy_call
from numba_opt.monte_carlo import price_european_call as numba_call
from multiprocessing_opt.monte_carlo import price_european_call as mp_call
from multithreading_opt.monte_carlo import price_european_call as mt_call

def run_benchmarks():
    implementations = {
        'Pure Python': baseline_call,
        'NumPy': numpy_call,
        'Numba': numba_call,
        'Multiprocessing': mp_call,
        'Multithreading': mt_call
    }
    
    # Try importing Cython
    try:
        # pyrefly: ignore [missing-import]
        from cython_opt.monte_carlo import price_european_call as cython_call
        implementations['Cython'] = cython_call
    except ImportError:
        print("Warning: Cython module not found. Build it using 'python setup.py build_ext --inplace' in cython_opt/")
        
    # Try importing C++
    try:
        # pyrefly: ignore [missing-import]
        from cpp_opt.monte_carlo_cpp import price_european_call as cpp_call
        implementations['C++ (pybind11)'] = cpp_call
    except ImportError:
        print("Warning: C++ pybind11 module not found. Build it using 'python setup.py build_ext --inplace' in cpp_opt/")

    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2
    paths = 2_000_000
    
    results = {}
    
    print(f"Running benchmarks with {paths:,} paths...\n")
    print(f"{'Implementation':<20} | {'Time (s)':<10} | {'Price':<10}")
    print("-" * 45)
    
    for name, func in implementations.items():
        if name == 'Numba':
            # Warm up JIT
            func(S0, K, T, r, sigma, 10)
            
        start_time = time.perf_counter()
        price = func(S0, K, T, r, sigma, paths)
        end_time = time.perf_counter()
        
        elapsed = end_time - start_time
        results[name] = elapsed
        print(f"{name:<20} | {elapsed:<10.4f} | {price:<10.4f}")
        
    # Plotting
    names = list(results.keys())
    times = list(results.values())
    
    plt.figure(figsize=(10, 6))
    plt.barh(names, times, color='skyblue')
    plt.xlabel('Execution Time (seconds)')
    plt.title(f'Monte Carlo Option Pricing Performance ({paths:,} paths)')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    
    plot_path = os.path.join(os.path.dirname(__file__), 'benchmark_results.png')
    plt.savefig(plot_path)
    print(f"\nPlot saved to {plot_path}")

if __name__ == '__main__':
    run_benchmarks()
