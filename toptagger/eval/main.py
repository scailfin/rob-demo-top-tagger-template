# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB) - Top Tagger Benchmark Demo Template.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Main evaluation routine. Adjust to your specific requirements."""

import numpy as np
import pickle
import random


def run_eval(datafile, weightsfile, resultfile, runs=5):
    """Dummy evaluation routine. Reads the weights file to ensure that it is
    accessible. Then generates a random result file.

    Parameters
    ----------
    datafile: string
        Path to file with pickled test data or result of pre-processing step.
    weightsfile: string
        Path to additional input file. Included for demonstration purposes.
        Remove if not needed.
    outfile: string
        Path to the output file.
    runs: int, default=5
        Number of runs in the output file.
    """
    # Read the weights file to ensure that we can access it.
    with open(weightsfile, 'r') as f:
        f.read()
    # Generate a random result file.
    with open(datafile, 'rb') as f:
        data = pickle.load(f, encoding='latin-1')
    output = np.empty((runs, len(data)))
    for x in range(runs):
        for y in range(len(data)):
            max_val = max(int(abs(data[y][0][0].max())), 1)
            output[x, y] = random.randint(0, max_val) / max_val
    with open(resultfile, 'wb') as f:
        pickle.dump(output, f)
