# Use Python 3.8 Image. Make sure to upgrade pip to latest version.
FROM python:3.8
RUN pip install --upgrade pip

# Copy source code files
COPY mytagger /app/mytagger
COPY requirements.txt /app/requirements.txt
COPY setup.py /app/setup.py

# Install the template package.
RUN pip install -r /app/requirements.txt
RUN pip install /app

# Copy data folder with additional data files
COPY mydata/ /mydata

WORKDIR /
