from model import SimpleNN
from trainer import ModelTrainer
from chat import chat

if __name__ == "__main__":
    input_size = 10
    hidden_size = 10
    output_size = 10

    model = SimpleNN(input_size, hidden_size, output_size)
    trainer = ModelTrainer(model)
    chat(trainer)
