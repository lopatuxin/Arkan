from utils import convert_to_vector, get_user_response


def chat(trainer):
    print("Аркан: Привет! Как я могу помочь?")

    while True:
        user_input = input("Ты: ").strip().lower()

        if user_input == "пока":
            print("Аркан: До встречи! Завершаю работу.")
            break

        input_vector = convert_to_vector(10)
        response = "ответ на основе модели"  # Упрощённая логика ответа

        print(f"Аркан: {response}")

        if not get_user_response():
            input("Введите правильный ответ: ")
            target_vector = convert_to_vector(10)
            trainer.train_step(input_vector, target_vector)
