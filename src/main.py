import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


# Простой класс нейросети
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Инициализация модели и оптимизатора
input_size = 10  # Размерность входа (количество признаков)
hidden_size = 10  # Размер скрытого слоя
output_size = 10  # Количество возможных ответов/меток
model = SimpleNN(input_size, hidden_size, output_size)
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Стохастический градиентный спуск


# Функция для обновления модели на лету
def update_model(input_vector, target_vector):
    model.train()  # Включаем режим обучения
    optimizer.zero_grad()  # Обнуляем градиенты
    output = model(input_vector)  # Прогоняем данные через модель
    loss = F.mse_loss(output, target_vector)  # Вычисляем ошибку
    loss.backward()  # Обратное распространение ошибки
    optimizer.step()  # Шаг оптимизации, обновление весов


# Пример интерактивного общения
def chat():
    while True:
        user_input = input("Ты: ").strip().lower()

        # Преобразуем ввод пользователя в числовой вектор
        # (Здесь пример упрощён, потребуется нормализация текста в вектор)
        input_vector = torch.randn(1, input_size)  # Случайный вектор для примера

        # Модель предсказывает ответ
        output_vector = model(input_vector)

        # Для простоты мы можем использовать тот же вектор как ответ
        response = "ответ на основе модели"

        print(f"Аркан: {response}")

        # Если бот не знает правильный ответ, он учится
        if input("Бот: Верный ответ? (да/нет): ").strip().lower() == "нет":
            correct_response = input("Введите правильный ответ: ")
            # Преобразуем правильный ответ в вектор (опять же, тут нужен реальный механизм)
            target_vector = torch.randn(1, output_size)  # Случайный вектор для примера
            update_model(input_vector, target_vector)  # Обновляем модель на лету

        # Завершение работы бота
        if user_input == "пока":
            print("Аркан: До встречи! Завершаю работу.")
            break


if __name__ == "__main__":
    chat()
