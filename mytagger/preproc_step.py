# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB) - Top Tagger Benchmark Demo Template.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""This is a dummy example for the Top Tagger pre-processing step. You can
adjust this example to your own requirements.

In this example, the pre-porcessor expects two arguments:

--testdata  Pickle file with test data sample.
--outfile   Output file for pre-processing results.
"""

import argparse
import os

from mytagger.preproc.main import run_preproc


if __name__ == '__main__':
    """Main routine for the pre-processor. Reads the command line arguments.
    Then calls the main pre-processing function in the preproc module.

    In this template implementation the pre-processor simply copies the input
    file to the output file.
    """
    # Get command line parameters. The pre-processor expects two inputs that
    # both are references to files.
    parser = argparse.ArgumentParser(
        description='Pre-processor for the ML4Jets Top Tagger evaluation.'
    )
    parser.add_argument(
        '-t', '--testdata',
        required=True,
        help='Test data sample file.'
    )
    parser.add_argument(
        '-o', '--outfile',
        required=True,
        help='Output file.'
    )
    args = parser.parse_args()
    # Call the main pre-processing function with the two arguments.
    run_preproc(
        testdatafile=args.testdata,
        outfile=args.outfile
    )
    # Ensure that the output file exists.
    assert os.path.isfile(args.outfile)
