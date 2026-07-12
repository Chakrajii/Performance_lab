#include <pybind11/pybind11.h>
#include <cmath>
#include <random>

namespace py = pybind11;

double price_european_call(double S0, double K, double T, double r, double sigma, int num_paths) {
    double sum_payoffs = 0.0;
    double drift = (r - 0.5 * sigma * sigma) * T;
    double vol = sigma * std::sqrt(T);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<double> d(0.0, 1.0);

    for (int i = 0; i < num_paths; ++i) {
        double z = d(gen);
        double ST = S0 * std::exp(drift + vol * z);
        double payoff = ST - K;
        if (payoff > 0) {
            sum_payoffs += payoff;
        }
    }

    return std::exp(-r * T) * (sum_payoffs / num_paths);
}

PYBIND11_MODULE(monte_carlo_cpp, m) {
    m.doc() = "pybind11 plugin for Monte Carlo Option Pricing";
    m.def("price_european_call", &price_european_call, "Prices a European Call option");
}
