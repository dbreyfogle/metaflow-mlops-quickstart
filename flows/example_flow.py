from metaflow import FlowSpec, Parameter, pypi, schedule, step


# Runs every 5 minutes when pushed to Step Functions
@schedule(cron="0/5 * * * ? *")
class ExampleFlow(FlowSpec):

    multiplier = Parameter("multiplier", default=10)

    @step
    def start(self):
        self.message = "Starting!"
        print(self.message)
        self.next(self.process)

    @pypi(packages={"numpy": "2.1.0"})
    @step
    def process(self):
        import numpy as np  # pylint: disable=import-error

        self.my_data = np.random.rand(3, 3)
        self.my_data_tf = self.multiplier * self.my_data
        print("Processed data!")
        self.next(self.end)

    @step
    def end(self):
        self.message = "Finished!"
        print(self.message)


if __name__ == "__main__":
    ExampleFlow()
