# trivia.py

class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
def run_quiz():
    quiz = Quiz()

    # Agregamos algunas preguntas de prueba
    quiz.add_question(Question("¿Cual es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], "París"))
    quiz.add_question(Question("¿Cual es el R=resultado de 3 x 3?", ["6", "9", "12", "3"], "9"))
    quiz.add_question(Question("¿Quien gano la copa del mundo 2022?", ["Peru", "Francia", "Brasil", "Argentina"], "Argentina"))

    print("Bienvenido al juego de trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.\n")

    score = 0
    total = 0

    while True:
        question = quiz.get_next_question()
        if not question:
            break

        print(f"Pregunta {total + 1}: {question.description}")
        for i, option in enumerate(question.options, 1):
            print(f"{i}) {option}")

        answer = input("Tu respuesta: ").strip()

        try:
            selected_option = question.options[int(answer) - 1]
        except (ValueError, IndexError):
            print("Opción inválida. Se marcará como incorrecta.")
            selected_option = None

        if selected_option and question.is_correct(selected_option):
            print("¡Correcto!\n")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {question.correct_answer}\n")

        total += 1

    print(f"\nJuego terminado. Aquí está tu puntuación:")
    print(f"Preguntas contestadas: {total}")
    print(f"Respuestas correctas: {score}")
    print(f"Respuestas incorrectas: {total - score}")
