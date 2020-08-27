# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB) - Top Tagger Benchmark Demo Template.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""This is a dummy example for the Top Tagger tagging step. You can adjust
this example to your own requirements.

In this example, the evaluation function expects three arguments:

--datafile  Pickle file with test data sample or the data file that was
            created by the pre-porcessing step.
--weights   Dummy text file for additional data that the evaluatormay need to
            access. This is to given an example how additional data can be
            accessed by your code. It is recommended to store all additional
            files that are needed by your implementation in the data/ folder
            of the template repository.
--outfile   Output file containing the evaluation results.
"""

import argparse
import os

from toptagger.tagger.main import run_tagger


if __name__ == '__main__':
    """Main routine for the tagger. Reads the command line arguments. Then
    calls the main tagger function in the respective tagger module.

    In this example implementation for the tagger simply reads the weights
    file to ensure that it is accessible and then generates a random result
    file.
    """
    # Get command line parameters. The pre-processor expects three input
    # parameters that all reference files.
    parser = argparse.ArgumentParser(
        description='Tagger for the ML4Jets Top Tagger evaluation.'
    )
    parser.add_argument(
        '-d', '--datafile',
        required=True,
        help='Test data sample file or pre-processing results file.'
    )
    parser.add_argument(
        '-w', '--weights',
        required=True,
        help='Dummy weigth file.'
    )
    parser.add_argument(
        '-r', '--runs',
        type=int,
        default=5,
        help='Number of runs in the output.'
    )
    parser.add_argument(
        '-o', '--outfile',
        required=True,
        help='Tagger result file.'
    )
    args = parser.parse_args()
    # Call the main tagger function with the three arguments.
    run_tagger(
        datafile=args.datafile,
        weightsfile=args.weights,
        resultfile=args.outfile,
        runs=args.runs
    )
    # Ensure that the output file exists.
    assert os.path.isfile(args.outfile)
