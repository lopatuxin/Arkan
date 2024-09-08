import torch


def convert_to_vector(text, vocab):
    indices = [vocab.get(word, 0) for word in text.lower().split()]
    return torch.tensor(indices)  # Замените на реальную логику векторизации


def get_user_response():
    response = input("Бот: Верный ответ? (да/нет): ").strip().lower()
    return response == "да"
