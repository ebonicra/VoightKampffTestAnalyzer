import json
from analyze_responses import analyze_physiological_responses


class VoightKampffTest:
    """Voight-Kampff Test (VK Test) is a fictional psychological assessment used 
    in the universe of "Blade Runner". It is designed to distinguish between humans 
    and replicants, which are bioengineered beings designed to resemble humans.

    This class represents the implementation of the Voight-Kampff Test in a Python 
    program. It simulates the administration of the test by prompting the user with 
    a series of questions and recording their responses, including physiological 
    indicators such as breathing rate, pulse rate, blushing intensity, and pupil dilation.

    Attributes:
        user_responses (dict): A dictionary containing user information, responses to 
            questions, and physiological responses recorded during the test."""

    def __init__(self) -> None:
        """Initialize the test object."""
        self.user_responses = {"user": '', "responses": [], "physiological_responses": {
            "breathing_rate": [], "pulse_rate": [], "blushing_intensity": [], "pupil_dilation": []}}

    def welcome_user(self) -> None:
        """Welcome the user to the Voight-Kampff test."""
        print("Добро пожаловать в тест Войта-Кампфа!")
        print("Этот тест поможет определить ваш уровень эмпатии и человечности.")
        self.user = input("Введите ваше имя: ")
        self.user_responses["user"] = self.user
        print(f"Привет, {self.user}! Готовы начать тест?\n")

    def load_questions(self, filename: str) -> dict:
        """Load questions from a JSON file.

        :param filename: The name of the file containing questions.
        :return: A dictionary containing question data.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                questions_data = json.load(file)
            if not questions_data:
                raise ValueError("Файл с вопросами пуст.")
            return questions_data
        except FileNotFoundError:
            raise FileNotFoundError("Файл с вопросами не найден.")
        except json.JSONDecodeError:
            raise ValueError("Некорректный формат файла с вопросами.")

    def ask_question(self, question: str, answers: list[str]) -> str:
        """Ask a question and return the user's answer.

        :param question: The text of the question.
        :param answers: A list of answer options.
        :return: The user's answer.
        """
        while True:
            print(question)
            for i, answer in enumerate(answers, start=1):
                print(f"{i}. {answer}")

            try:
                choice = int(input("Выберите ответ (введите номер ответа): "))
                if 1 <= choice <= 4:
                    break
                else:
                    raise ValueError("Ответ должен быть в пределах от 1 до 4.")
            except ValueError as e:
                print("Ошибка: ", e)
                print("Пожалуйста, введите корректное значение.\n")
        return choice

    def physiological_responses(self) -> None:
        """Record the user's physiological responses after the questions.

        :param questions: A dictionary containing questions and answer options.
        """
        for param in self.user_responses["physiological_responses"]:
            while True:
                try:
                    if param == "breathing_rate":
                        breathing_rate = int(input(
                            "Введите частоту дыхания (приблизительный диапазон от 12 до 16 вдохов в минуту): "))
                        if breathing_rate < 10 or breathing_rate > 25:
                            raise ValueError(
                                "Частота дыхания должна быть в диапазоне от 10 до 25 вдохов в минуту.")
                        else:
                            self.user_responses["physiological_responses"]["breathing_rate"].append(
                                breathing_rate)
                            break

                    elif param == "pulse_rate":
                        pulse_rate = int(
                            input("Введите пульс (приблизительный диапазон от 60 до 100 ударов в минуту): "))
                        if pulse_rate < 50 or pulse_rate > 150:
                            raise ValueError(
                                "Пульс должен быть в диапазоне от 50 до 150 ударов в минуту.")
                        else:
                            self.user_responses["physiological_responses"]["pulse_rate"].append(
                                pulse_rate)
                            break

                    elif param == "blushing_intensity":
                        blushing_intensity = float(input(
                            "Введите интенсивность покраснений (приблизительный диапазон от 1 до 6): "))
                        if blushing_intensity < 1 or blushing_intensity > 6:
                            raise ValueError(
                                "Интенсивность покраснений должна быть в диапазоне от 1 до 6.")
                        else:
                            self.user_responses["physiological_responses"]["blushing_intensity"].append(
                                blushing_intensity)
                            break

                    elif param == "pupil_dilation":
                        pupil_dilation = float(
                            input("Введите расширение зрачков (приблизительный диапазон от 2 до 8 мм): "))
                        if pupil_dilation < 2 or pupil_dilation > 10:
                            raise ValueError(
                                "Размер значков должен быть в диапазоне от 2 до 10 мм.")
                        else:
                            self.user_responses["physiological_responses"]["pupil_dilation"].append(
                                pupil_dilation)
                            break
                except ValueError as e:
                    print("Ошибка: ", e)
                    print("Пожалуйста, введите корректное значение.\n")

    def record_responses(self, questions: dict) -> None:
        """Record the user's responses to the questions."""
        for i, question_data in enumerate(questions, start=1):
            question = question_data['question']
            answers = list(question_data['answers'].values())

            user_answer = self.ask_question(question, answers)
            self.user_responses["responses"].append(
                {"question": question, "answer": user_answer})
            print()
            self.physiological_responses()
            print()

    def save_user_responses(self) -> None:
        """Save the user's responses to a JSON file."""
        with open('user_responses.json', 'w', encoding='utf-8') as file:
            json.dump(self.user_responses, file, ensure_ascii=False, indent=4)

    def analyze_user_responses(self) -> None:
        """Analyze the user's physiological responses and determine the result."""
        result = analyze_physiological_responses(
            self.user_responses["physiological_responses"])
        print(f"Результат теста: ВЫ - {result.upper()}!")


def main() -> None:
    """Main function for executing the test."""
    test = VoightKampffTest()
    test.welcome_user()
    questions = test.load_questions('questions.json')
    test.record_responses(questions)
    test.save_user_responses()
    test.analyze_user_responses()


if __name__ == "__main__":
    main()
