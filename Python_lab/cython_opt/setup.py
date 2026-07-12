from setuptools import setup
# pyrefly: ignore [missing-import]
from Cython.Build import cythonize

setup(
    name='monte_carlo_cython',
    ext_modules=cythonize("monte_carlo.pyx", compiler_directives={'language_level' : "3"})
)
