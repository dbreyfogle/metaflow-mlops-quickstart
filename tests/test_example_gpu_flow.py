from metaflow import Runner

from flows.config import (
    BATCH_GPU_QUEUE,
    METAFLOW_PACKAGE_SUFFIXES,
    METAFLOW_TEST_NAMESPACE,
)


def test_example_gpu_flow():
    with Runner(
        "flows/example_gpu_flow.py",
        environment="pypi",
        decospecs=[f"batch:queue={BATCH_GPU_QUEUE}"],
        env={
            "METAFLOW_PACKAGE_SUFFIXES": METAFLOW_PACKAGE_SUFFIXES,
            "METAFLOW_USER": METAFLOW_TEST_NAMESPACE,
        },
    ).run() as running:
        assert running.run.data.gpu_detected
