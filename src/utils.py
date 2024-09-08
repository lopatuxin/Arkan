import torch


def convert_to_vector(text, phrase_processor):
    indices = phrase_processor.process_phrase(text)
    return torch.tensor(indices)


def get_user_response():
    response = input("Бот: Верный ответ? (да/нет): ").strip().lower()
    return response == "да"
