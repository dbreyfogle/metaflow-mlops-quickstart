import numpy as np
from metaflow import Runner
from pytest import approx


def test_example_flow():
    with Runner("flows/example_flow.py", environment="pypi", decospecs=["batch"]).run(
        multiplier=5
    ) as running:
        multiplier = running.run.data.multiplier
        my_data = running.run.data.my_data
        my_data_tf = running.run.data.my_data_tf
        assert multiplier * np.mean(my_data) - np.mean(my_data_tf) == approx(0)
        assert multiplier * np.std(my_data) - np.std(my_data_tf) == approx(0)
