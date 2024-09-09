from src.utils.utils import convert_to_vector, get_user_response


def chat(trainer, phrase_processor):
    print("Аркан: Привет! Как я могу помочь?")

    while True:
        user_input = input("Ты: ").strip().lower()

        if user_input == "пока":
            print("Аркан: До встречи! Завершаю работу.")
            break

        # Преобразуем входной текст в вектор индексов
        input_vector = convert_to_vector(user_input, phrase_processor).unsqueeze(0)  # Добавляем размер батча
        response_vector = trainer.model(input_vector)  # Получаем ответ от модели (упрощённая логика ответа)

        # Преобразуем выходной вектор модели в текст
        response_text = phrase_processor.decode_vector(response_vector.argmax(dim=1))  # Используем argmax для выбора наилучшего ответа
        print(f"Аркан: {response_text}")

        if not get_user_response():
            correct_answer = input("Введите правильный ответ: ").strip().lower()
            target_vector = convert_to_vector(correct_answer, phrase_processor).unsqueeze(0).float()  # Целевой вектор
            print(f"Target shape: {target_vector.shape}")
            trainer.train_step(input_vector, target_vector)  # Обучение модели на новом примере
