def main():
    print("Аркан запущен и готов к работе!")

    commands = {
        "привет": "Приветствую! Чем могу помочь?",
        "помощь": "Я умею откликаться на команды: привет, помощь, пока.",
        "пока": "До встречи! Аркан завершает работу."
    }

    while True:
        try:
            user_input = input("Ты: ")

            # Простая обработка команд
            response = commands.get(user_input.lower(), "Не понимаю эту команду.")

            print(f"Аркан: {response}")

            # Завершение работы при команде "пока"
            if user_input.lower() == "пока":
                break

        except (KeyboardInterrupt, EOFError):
            print("\nАркан завершает работу.")
            break


if __name__ == "__main__":
    main()
