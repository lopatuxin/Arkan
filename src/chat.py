from utils import convert_to_vector, get_user_response


def chat(trainer, vocab):
    print("Аркан: Привет! Как я могу помочь?")

    while True:
        user_input = input("Ты: ").strip().lower()

        if user_input == "пока":
            print("Аркан: До встречи! Завершаю работу.")
            break

        # Преобразуем входной текст в вектор индексов
        input_vector = convert_to_vector(user_input, vocab).unsqueeze(0)  # Добавляем размер батча
        response = trainer.model(input_vector)  # Получаем ответ от модели (упрощённая логика ответа)

        print(f"Аркан: {response}")

        if not get_user_response():
            correct_answer = input("Введите правильный ответ: ")
            target_vector = convert_to_vector(correct_answer, vocab).unsqueeze(0)  # Целевой вектор
            trainer.train_step(input_vector, target_vector)  # Обучение модели на новом примере
