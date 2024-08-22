from metaflow import Runner


def test_example_gpu_flow():
    with Runner("flows/example_gpu_flow.py", decospecs=["batch"]).run() as running:
        assert running.run.data.gpu_detected
