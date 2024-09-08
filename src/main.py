from model import SimpleNN
from src.database import VocabularyDatabase
from src.phrase_processor import PhraseProcessor
from trainer import ModelTrainer
from chat import chat

# Инициализация базы данных и обработчика фраз
vocab_db = VocabularyDatabase()
phrase_processor = PhraseProcessor(vocab_db)

# Инициализация модели
input_size = 10  # Размер словаря
embedding_dim = 10  # Размерность эмбеддингов
hidden_size = 10  # Количество нейронов в скрытом слое
output_size = 10  # Количество выходных признаков (например, для классификации)

# Создание экземпляра модели
model = SimpleNN(input_size, embedding_dim, hidden_size, output_size)

# Инициализация тренера модели
trainer = ModelTrainer(model)

# Запуск чата
if __name__ == "__main__":
    chat(trainer, phrase_processor)
