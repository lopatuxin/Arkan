import torch


def convert_to_vector(text, phrase_processor):
    indices = phrase_processor.process_phrase(text)
    tensor = torch.tensor(indices)
    return tensor


def get_user_response():
    response = input("Бот: Верный ответ? (да/нет): ").strip().lower()
    return response == "да"
