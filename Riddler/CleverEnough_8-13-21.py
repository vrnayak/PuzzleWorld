# Date: August 13th, 2021
# Type: Express
# Name: Are You Clever Enough?
#
# Description: You are in the top 10 percent of puzzle solvers in Riddler Nation.
#              You don't know where exactly in that 10 percent you are, but suppose
#              you are equally likely to be anywhere within that group. Suppose
#              further that no two people in Riddler Nation are equally clever.
#              If you walk into a room with nine other members of Riddler Nation,
#              what is the probability that you are the cleverest solver in the room?

import math
import numpy as np

N = 20               # number of other members in the room
Top = 0.1           # top percentile group that you are in (expressed as decimal)
Trials = 1000000    # number of trials to determine probability 


# this function is vectorized for speed
def simulate():

    your_percentile = np.random.rand(Trials) * Top + (1 - Top)
    other_percentiles = np.random.rand(N, Trials)
    num_times_cleverest = np.count_nonzero((your_percentile > other_percentiles).all(axis=0))
    return num_times_cleverest / Trials


def solve():

    probability = 0.0
    for k in range(N):
        probability += math.comb(N, k) * pow(Top, k) * pow(1 - Top, N - k) * (1 / (k + 1))
    return probability


def main():

    sim_probability = simulate()
    true_probability = solve()
    print("Simulated probability of being cleverest: {:.4f}".format(sim_probability))
    print("True probability of being cleverest: {:.4f}".format(true_probability))


if __name__ == '__main__':
    main()
