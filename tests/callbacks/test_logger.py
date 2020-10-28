from tempfile import TemporaryDirectory
from unittest import skipIf
from unittest.mock import call

import torch
import torch.nn as nn
from poutyne.framework import Model

from ptcallbacks.callbacks import MlFlowWriter

try:
    import mlflow as mlflow
except ImportError:
    mlflow = None


def some_data_generator(batch_size):
    while True:
        x = torch.rand(batch_size, 1)
        y = torch.rand(batch_size, 1)
        yield x, y


@skipIf(mlflow is None, "Needs tensorboardX to run this test")
class MLFlowWriterTest:
    batch_size = 20
    lr = 1e-3
    num_epochs = 10

    def setUp(self):
        torch.manual_seed(42)
        self.pytorch_network = nn.Linear(1, 1)
        self.loss_function = nn.MSELoss()
        self.optimizer = torch.optim.SGD(self.pytorch_network.parameters(), lr=MLFlowWriterTest.lr)
        self.model = Model(self.pytorch_network, self.optimizer, self.loss_function)
        self.temp_dir_obj = TemporaryDirectory()

    def tearDown(self):
        self.temp_dir_obj.cleanup()

    def test_writing(self):
        train_gen = some_data_generator(20)
        valid_gen = some_data_generator(20)
        writer = MlFlowWriter(experiment_name="test_name", tracking_path="")
        history = self.model.fit_generator(train_gen,
                                           valid_gen,
                                           epochs=self.num_epochs,
                                           steps_per_epoch=5,
                                           callbacks=[writer])
        self._test_writing(history)

    def _test_writing(self, history):
        calls = list()
        for h in history:
            calls.append(call('loss', {'loss': h['loss'], 'val_loss': h['val_loss']}, h['epoch']))
            calls.append(call('lr', {'lr': self.lr}, h['epoch']))
        self.writer.add_scalars.assert_has_calls(calls, any_order=True)
