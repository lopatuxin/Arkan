import torch.nn.functional as func
import torch.optim as optim


class ModelTrainer:
    def __init__(self, model, learning_rate=0.01):
        self.model = model
        self.optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    def train_step(self, input_vector, target_vector):
        self.model.train()
        self.optimizer.zero_grad()
        output = self.model(input_vector)
        loss = func.mse_loss(output, target_vector)
        loss.backward()
        self.optimizer.step()
