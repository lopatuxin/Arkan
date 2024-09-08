import torch.nn as nn
import torch.nn.functional as func


class SimpleNN(nn.Module):
    def __init__(self, hidden_size, output_size, vocab_size, embedding_dim):
        super(SimpleNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.fc1 = nn.Linear(embedding_dim, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.embedding(x)
        x = x.mean(dim=1)
        x = func.relu(self.fc1(x))
        return self.fc2(x)
