from model import SimpleNN
from trainer import ModelTrainer
from chat import chat

# Создание словаря (в реальном проекте он может быть заранее определённым или обученным)
vocab = {'привет': 1, 'как': 2, 'дела': 3, 'все': 4, 'хорошо': 5, 'спасибо': 6}

# Инициализация модели
input_size = len(vocab)  # Размер словаря
embedding_dim = 10  # Размерность эмбеддингов
hidden_size = 10  # Количество нейронов в скрытом слое
output_size = 10  # Количество выходных признаков (например, для классификации)

# Создание экземпляра модели
model = SimpleNN(input_size, embedding_dim, hidden_size, output_size)

# Инициализация тренера модели
trainer = ModelTrainer(model)

# Запуск чата
if __name__ == "__main__":
    chat(trainer, vocab)
