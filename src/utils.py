import torch


def convert_to_vector(input_size):
    """
    Заглушка для функции, преобразующей текстовый ввод в тензорный вектор.
    Требуется реализация нормализации текста и векторизации.
    """
    return torch.randn(1, input_size)  # Замените на реальную логику векторизации


def get_user_response():
    response = input("Бот: Верный ответ? (да/нет): ").strip().lower()
    return response == "да"
