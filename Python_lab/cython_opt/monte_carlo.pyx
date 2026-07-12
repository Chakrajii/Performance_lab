from libc.math cimport exp, sqrt, log, cos
from libc.stdlib cimport rand, RAND_MAX
import math

cdef double pi = math.pi

cdef double random_gauss():
    """Generates a standard normal random variable using Box-Muller transform."""
    cdef double u1 = (rand() + 1.0) / (RAND_MAX + 1.0)
    cdef double u2 = (rand() + 1.0) / (RAND_MAX + 1.0)
    cdef double z0 = sqrt(-2.0 * log(u1)) * cos(2.0 * pi * u2)
    return z0

cpdef double price_european_call(double S0, double K, double T, double r, double sigma, int num_paths):
    cdef double sum_payoffs = 0.0
    cdef double drift = (r - 0.5 * sigma**2) * T
    cdef double vol = sigma * sqrt(T)
    cdef double z, ST, payoff
    cdef int i
    
    for i in range(num_paths):
        z = random_gauss()
        ST = S0 * exp(drift + vol * z)
        payoff = ST - K
        if payoff > 0:
            sum_payoffs += payoff
            
    return exp(-r * T) * (sum_payoffs / num_paths)
