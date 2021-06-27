from ratings.lattice.lattice_bayes import std_posterior_dividend
import math


def test_posterior():
    dividends = [2, 3, 6]
    observations = [0, -1, -0.5]
    pseudo = std_posterior_dividend(dividends=dividends, ability_std=10, performance_std=2 * math.sqrt(2),
                                    observations=observations)
    print(pseudo)