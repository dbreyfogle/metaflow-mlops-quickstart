from config import BATCH_GPU_QUEUE, CONFIG_DEPS, ECR_PATH
from metaflow import FlowSpec, batch, pypi, pypi_base, step

IMAGE = f"{ECR_PATH}/pytorch-extras:2.4.0-cuda12.4-cudnn9-runtime"


@pypi_base(packages=CONFIG_DEPS)
class ExampleGPUFlow(FlowSpec):

    @batch(gpu=1, queue=BATCH_GPU_QUEUE, image=IMAGE)
    @pypi(disabled=True)
    @step
    def start(self):
        import torch  # pylint: disable=import-error

        if torch.cuda.is_available():
            self.gpu_detected = True
            print("GPU is available!")
        else:
            self.gpu_detected = False
            print("GPU is NOT available!")
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    ExampleGPUFlow()
