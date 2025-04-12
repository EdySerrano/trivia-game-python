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
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False

    
def run_quiz():
    quiz = Quiz()

    for _ in range(10):
        quiz.add_question(Question("¿Cual es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], "París"))
        quiz.add_question(Question("¿Cual es el R=resultado de 3 x 3?", ["6", "9", "12", "3"], "9"))
        quiz.add_question(Question("¿Quien gano la copa del mundo 2022?", ["Peru", "Francia", "Brasil", "Argentina"], "Argentina"))
        quiz.add_question(Question("¿Cuál es la capital de Australia?", ["Sídney", "Melbourne", "Canberra", "Brisbane"], "Canberra"))
        quiz.add_question(Question("¿Quién pintó la Mona Lisa?", ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"], "Da Vinci"))
        quiz.add_question(Question("¿Cuál es el planeta más grande del sistema solar?", ["Tierra", "Saturno", "Júpiter", "Marte"], "Júpiter"))
        quiz.add_question(Question("¿En qué año son las proximas elecciones presidenciales en el Peru?", ["2025","2026" "2027", "2028"], "2026"))
        quiz.add_question(Question("¿Quién escribió 'Cien años de soledad'?", ["Mario Vargas Llosa", "Pablo Neruda", "Gabriel García Márquez", "Julio Ramon Riveiro"], "Gabriel García Márquez"))
        quiz.add_question(Question("¿Qué gas respiramos que es esencial para la vida humana?", ["Hidrógeno", "Oxígeno", "Dióxido de carbono", "Nitrógeno"], "Oxígeno"))
        quiz.add_question(Question("¿Cuál es el océano más grande del mundo?", ["Atlántico", "Índico", "Ártico", "Pacífico"], "Pacífico"))
    print("Bienvenido al juego de trivia!")
    print("Responde 10 preguntas.\n")

    rounds = 0
    while rounds < 10:
        question = quiz.get_next_question()
        if not question:
            break

        print(f"Pregunta {rounds + 1}: {question.description}")
        for i, option in enumerate(question.options, 1):
            print(f"{i}) {option}")

        answer = input("Tu respuesta: ").strip()

        try:
            selected_option = question.options[int(answer) - 1]
        except (ValueError, IndexError):
            print("Opción inválida. Se marcará como incorrecta.")
            selected_option = None

        is_correct = quiz.answer_question(question, selected_option) if selected_option else False

        if is_correct:
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta era: {question.correct_answer}\n")

        rounds += 1

    print("\nJuego terminado.")
    print(f"Preguntas contestadas: 10")
    print(f"Correctas: {quiz.correct_answers}")
    print(f"Incorrectas: {quiz.incorrect_answers}")



    