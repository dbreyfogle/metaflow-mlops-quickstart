# DO NOT INCLUDE ANY SENSITIVE INFORMATION IN THIS FILE!

# This file is used to store shared/reusable configs across Metaflow runs.
# See https://docs.metaflow.org/scaling/dependencies/project-structure.

# If you import this module, make sure to supply the required dependencies
# using appropriate pypi/conda decorators, or by providing a Docker image.
# >> @pypi_base(packages=CONFIG_DEPS)

# This module reads environment variables from the .env file.
# If your flow does any remote execution, you will need to pass
# your .env file using --package-suffixes=.env, or you can set
# METAFLOW_PACKAGE_SUFFIXES=.env in your environment variables. Make
# sure .env is symlinked to the same directory containing your flow.
# >> python my_flow.py --environment=pypi --package-suffixes=.env run

CONFIG_DEPS = {"python-dotenv": "1.0.1"}

import os

from dotenv import load_dotenv

load_dotenv()


CFN_STACK_NAME = os.getenv("CFN_STACK_NAME")

BATCH_GPU_QUEUE = f"{CFN_STACK_NAME}-gpu"

METAFLOW_PACKAGE_SUFFIXES = ".env"
