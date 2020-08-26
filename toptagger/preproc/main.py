# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB) - Top Tagger Benchmark Demo Template.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Main pre-processing routing. Adjust to your specific requirements."""

import shutil


def run_preproc(testdatafile, outfile):
    """Dummy pre-processing routine. Copies the testdata file to the outfile.

    Parameters
    ----------
    testdatafile: string
        Path to file with pickled test data.
    outfile: string
        Path to the output file.
    """
    # Copy the testdata file to the output file.
    shutil.copy(src=testdatafile, dst=outfile)
