=======================================================
Reproducible Open Benchmarks - Top Tagger Demo Template
=======================================================

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://github.com/scailfin/rob-demo-top-tagger-template/blob/master/LICENSE



About
=====

The **Top Tagger Demo Template** is part of the `Reproducible Open Benchmarks for Data Analysis Platform (ROB) <https://github.com/scailfin/rob-ui>`_. This repository contains the template layout for participants in the `Reproducible Open Benchmarks - Top Tagger Demo <https://github.com/scailfin/rob-demo-top-tagger>`_. You can use this template to package your contribution code into a Docker container that can then be used to run the benchmark demo.


Top Tagger Workflow
===================

The idea of `The Machine Learning Landscape of Top Taggers <https://arxiv.org/abs/1902.09914>`_ comparison is to see how well different neutral network setups can classify jets based on calorimeter information. Participants in the comparison would train and evaluate different models using the `Top Tagging Reference Dataset <https://docs.google.com/document/d/1Hcuc6LBxZNX16zjEGeq16DAzspkDC4nDTyjMp1bWHRo/edit>`_ . For the `Top Tagger Evaluation Workflow for the ML4Jets Demo <https://raw.githubusercontent.com/scailfin/presentations/master/slides/ROB-ML4Jets.pdf>`_ we used a smaller subset of the original data. The demo is only focused on the evaluation step. The initial training phase has to be done beforehand.

The evaluation workflow for the demo consist of 3 steps.

- Pre-Processing: This is an (optional) pre-processing step in which you can transform or adjust the test data sample to fit the the format required by your tagger code. This template contains a dummy implementation for a pre-processor that you can use if your tagger does not require pre-processing but operates on the original test data sample, instead.
- Tagger: ???
- Scoring: To compare different model outputs, single-number performance metrics are evaluated on the test sample. These metrics include the area under the ROC curve (AUC), and the background rejection at a signal efficiency of 50% the background rejection mean from an ensemble tagger setup.

Participants in the benchmark have to provide an implementation for the tagger and (if required) for the pre-processing step. The final scoring step in the workflow is common to all participants and cannot be changed.

The format of the test data sample is ???. The expected output of the tagger is ???.

The test data sample file is the only file that is available by default to your tagger. All other files that your code may require have to be included in the Docker container (see below for details).



Template Repository Structure
=============================

This repository contains code stumps for the pre-processing and tagger steps in the workflow. The entry point for pre-processing is ``mytagger/preproc_step.py`` and for the tagger the entry point is ``mytagger/tagger_step.py``. You can use the files as the starting point to include the code for your trained model. It is recommended that you place your own code files in the respective folders ``preproc`` and ``tagger`` of the ``mytagger`` package in the repository.

If your tagger does not require a pre-processing step you can use the ``mytagger/do-nothing.py`` module for the first step in the workflow (see below).

If your pre-processor or tagger requires access to additional data files, these should be placed in the ``mydata`` folder of the repository. When running the workflow steps in the `ROB Framework <https://github.com/scailfin/rob-ui>`_, these files will be accessible at the base path ``/mydata``.

Make sure to include all dependencies for your Python environment in the ``requirements.txt`` file. Before starting development you should run the following commands (from the root directory of the repository) in your virtual Python environment:

.. code-block:: bash

    pip install -r requirements.txt
    pip install -e .


Packaging Your Code
===================

When you are finished with testing your code, everything has to be packed into a Docker image. The repository contains a Dockerfile that will do the job for you. Use the following command to create the Docker image (from the root directory of the repository):

.. code-block:: bash

    docker image build -t mytoptagger .

This will create a Docker image *mytoptagger* on your machine. If this is the same machin on which you are running the ROB framework everything should be fine. Otherwise, you will need to push the image to DockerHub first (see example below):

.. code-block:: bash

    docker image tag mytoptagger myusername/mytoptagger
    docker image push myusername/mytoptagger



Running Your Code in ROB
========================

When running the Top Tagger Demo Workflow in the `ROB User Interface <https://github.com/scailfin/rob-ui>`_ you see a submission form that requires you to enter four argument values. The respective form fields are pre-filled with the default values (as shown in the screen shot below):

.. image:: docs/graphics/submit-form.jpg
    :align: center
    :alt: ROB Workflow Run Submission Screenshot


There are two parameters for each step of the workflow. The first parameter (Environment) is the identifier of your Docker image (e.g., ``mytoptagger`` or ``myusername/mytoptagger``). The second parameter (Command) is the command-line command to run your code for the respective workflow step. Below are example commands. Note that these commands will have to be adjusted if you change the input arguments for either of the two workflow steps. **The important thing to keep in mind** is that the output file for the tagger step **has to be called** ``/results/yProbBest.pkl``. This is the file that the final step in the workflow will use to compute scores for run results.

Command-Line for Pre-Processing Step
------------------------------------

If you use the given pre-processor stub, the command to run this step is:

.. code-block:: bash

    python app/mytagger/preproc_step.py -t data/test_jets.pkl -o results/preproc_test_jets.pkl

If your code does not require pre-processing you can use the ``do_nothing.py`` module to *run* this workflow step:

.. code-block:: bash

    python app/mytagger/do_nothing.py


Command-Line for Tagger Step
----------------------------

Depending on whether your tagger operates on the original test data sample or the pre-processing result the command for the tagger step is either one of the following two.

Run tagger on pre-processing results.

.. code-block:: bash

    python app/mytagger/tagger_step.py -d results/preproc_test_jets.pkl -w mydata/my_data.txt -o results/yProbBest.pkl

Run tagger on original test data sample.

.. code-block:: bash

    python app/mytagger/tagger_step.py -d data/test_jets.pkl -w mydata/my_data.txt -o results/yProbBest.pkl


Again, these commands are for the stubs that are included in the repository. Adjust them accordingly if you change the input arguments for your own code.

To test that everything works, you can run the packaging code and the command-line examples directly after cloning this repository on your local machine. Make sure that you use the Docker workflow engine when you configure your local instance of ROB:

.. code-block:: bash

    # Note that this demo requires a running Docker Daemon on your machine.
    export FLOWSERV_BACKEND_MODULE=flowserv.controller.serial.docker
    export FLOWSERV_BACKEND_CLASS=DockerWorkflowEngine
