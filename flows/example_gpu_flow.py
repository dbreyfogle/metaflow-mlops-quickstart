from metaflow import FlowSpec, batch, step

CFN_STACK_NAME = "metaflow"


class ExampleGPUFlow(FlowSpec):

    @batch(
        gpu=1,
        image="docker.io/pytorch/pytorch:2.4.0-cuda12.4-cudnn9-runtime",
        queue=f"{CFN_STACK_NAME}-gpu",
    )
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
