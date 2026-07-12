# Python Performance Engineering Lab

A framework for systematically optimizing computationally intensive Python workloads while preserving algorithmic correctness. This lab explores and benchmarks multiple performance engineering techniques across diverse workloads, providing reproducible results and actionable insights.

---

## 📌 Objectives
- Identify CPU and memory bottlenecks in Python applications.
- Apply optimization techniques without altering algorithmic correctness.
- Benchmark execution time, memory consumption, CPU utilization, and scalability.
- Compare trade-offs between implementation complexity and performance gains.
- Automate benchmarking and generate reproducible performance reports.

---

## 🚀 Optimization Techniques
- **NumPy Vectorization** – Efficient array operations.
- **Numba JIT Compilation** – Accelerated Python functions.
- **Multiprocessing** – Parallel execution across cores.
- **Cython** – Compiled Python for speed.
- **C++ Extensions (pybind11)** – Native performance integration.

---

## 🛠 Profiling Tools
- `cProfile` – Function-level profiling.
- `line_profiler` – Line-by-line execution analysis.
- Memory profilers – Track memory allocation and leaks.

---

## 📊 Benchmarking & Reporting
- Automated benchmarking scripts.
- Comparative runtime and memory usage reports.
- Visualizations for performance-driven decision making.

---

## 📂 Project Structure

## ⚡ Getting Started

### Prerequisites
- Python 3.9+
- NumPy
- Numba
- Cython
- pybind11
- matplotlib (for visualizations)

### Installation
```bash
git clone https://github.com/your-username/performance-lab.git
cd performance-lab
pip install -r requirements.txt
```

### Run Benchmarks
python benchmarks/run_all.py

### Profile a Script
python -m cProfile -o profiling/output.prof benchmarks/example.py

