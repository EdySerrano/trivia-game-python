# trivia.py

from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

n    def is_correct(self, answer):
        return self.correct_answer == answer



def get_easy_questions():
    return [
        Question("¿Cual es la capital de Francia?", ["Madrid", "Londres", "París", "Berlín"], "París"),
        Question("¿Cual es el R=resultado de 3 x 3?", ["6", "9", "12", "3"], "9"),
        Question("¿Quien gano la copa del mundo 2022?", ["Peru", "Francia", "Brasil", "Argentina"], "Argentina"),
        Question("¿Cuál es la capital de Australia?", ["Sídney", "Melbourne", "Canberra", "Brisbane"], "Canberra"),
        Question("¿Quién pintó la Mona Lisa?", ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"], "Da Vinci"),
        Question("¿Cuál es el planeta más grande del sistema solar?", ["Tierra", "Saturno", "Júpiter", "Marte"], "Júpiter"),
        Question("¿En qué año son las proximas elecciones presidenciales en el Peru?", ["2025","2026" "2027", "2028"], "2026"),
        Question("¿Quién escribió 'Cien años de soledad'?", ["Mario Vargas Llosa", "Pablo Neruda", "Gabriel García Márquez", "Julio Ramon Riveiro"], "Gabriel García Márquez"),
        Question("¿Qué gas respiramos que es esencial para la vida humana?", ["Hidrógeno", "Oxígeno", "Dióxido de carbono", "Nitrógeno"], "Oxígeno"),
        Question("¿Cuál es el océano más grande del mundo?", ["Atlántico", "Índico", "Ártico", "Pacífico"], "Pacífico"),
    ]

def get_medium_questions():
    return [
        Question("¿Quién desarrolló la teoría de la relatividad?", ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Stephen Hawking"], "Albert Einstein"),
        Question("¿Cuál es el país con más medallas olímpicas en la historia?", ["Rusia", "China", "Estados Unidos", "Alemania"], "Estados Unidos"),
        Question("¿En qué año se firmó la Declaración de Independencia de EE.UU.?", ["1776", "1789", "1812", "1750"], "1776"),
        Question("¿Cuál es la fórmula química del agua?", ["H2O", "O2", "CO2", "NaCl"], "H2O"),
        Question("¿Cuál es la capital de Canadá?", ["Toronto", "Vancouver", "Ottawa", "Montreal"], "Ottawa"),
        Question("¿Qué instrumento mide la presión atmosférica?", ["Termómetro", "Barómetro", "Altímetro", "Higrómetro"], "Barómetro"),
        Question("¿Cuál es el idioma más hablado del mundo?", ["Inglés", "Español", "Hindi", "Chino mandarín"], "Chino mandarín"),
        Question("¿Quién fue el primer hombre en el espacio?", ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard"], "Yuri Gagarin"),
        Question("¿Qué país tiene forma de bota?", ["España", "Italia", "Grecia", "Turquía"], "Italia"),
        Question("¿Qué continente tiene más países?", ["Asia", "Europa", "África", "América"], "África"),

    ]

def get_hard_questions():
    return [
        Question("¿Qué científico propuso la teoría heliocéntrica?", ["Aristóteles", "Galileo Galilei", "Copérnico", "Kepler"], "Copérnico"),
        Question("¿Cuál es el elemento número 79 en la tabla periódica?", ["Oro", "Plomo", "Mercurio", "Uranio"], "Oro"),
        Question("¿Qué autor escribió 'En busca del tiempo perdido'?", ["Franz Kafka", "James Joyce", "Marcel Proust", "Fiódor Dostoyevski"], "Marcel Proust"),
        Question("¿Cuál es la velocidad de la luz en el vacío?", ["300,000 km/h", "150,000 km/s", "300,000 km/s", "1,080,000 km/h"], "300,000 km/s"),
        Question("¿Cuál fue la dinastía que unificó China en el año 221 a.C.?", ["Han", "Tang", "Qin", "Song"], "Qin"),
        Question("¿Qué compositor escribió la ópera 'La flauta mágica'?", ["Beethoven", "Mozart", "Bach", "Vivaldi"], "Mozart"),
        Question("¿Qué país inventó el papel moneda?", ["India", "Egipto", "China", "Persia"], "China"),
        Question("¿En qué año comenzó la Revolución Francesa?", ["1776", "1789", "1804", "1815"], "1789"),
        Question("¿Qué tipo de célula no tiene núcleo?", ["Animal", "Vegetal", "Procariota", "Eucariota"], "Procariota"),
        Question("¿Qué filósofo escribió 'El ser y la nada'?", ["Sartre", "Nietzsche", "Kant", "Heidegger"], "Sartre"),

     ]


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
    print("=" * 40)
    print("¡Bienvenido al juego de Trivia!")
    print("Selecciona un nivel de dificultad:")
    print("1) Fácil\n2) Medio\n3) Difícil")

    difficulty = input("Nivel (1/2/3): ").strip()

    print("=" * 40)
    print("Responde seleccionando el número de la opción correcta.")
    print("=" * 40)

    quiz = Quiz()

    if difficulty == "1":
        questions = get_easy_questions()
    elif difficulty == "2":
        questions = get_medium_questions()
    elif difficulty == "3":
        questions = get_hard_questions()
    else:
        print(" Nivel no válido. Se asignará nivel fácil por defecto.")
        questions = get_easy_questions()

    for q in questions:
        quiz.add_question(q)

    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        if question:
            print(f"\nPregunta {quiz.current_question_index}: {question.description}")
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer = input("Tu respuesta: ").strip()
            if answer == "":
                print(" Por favor ingresa un número.")
                continue
            if quiz.answer_question(question, answer):
                print(" ¡Correcto!")
            else:
                print(" Incorrecto.")
        else:
            break

    print("\n Juego terminado. Aquí está tu puntuación:")
    print(f"Preguntas contestadas: 10")
    print(f" Respuestas correctas: {quiz.correct_answers}")
    print(f" Respuestas incorrectas: {quiz.incorrect_answers}")



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/questions/easy")
def get_easy():
    questions = get_easy_questions()
    return [{"description": q.description, "options": q.options} for q in questions]

@app.get("/questions/medium")
def get_medium():
    questions = get_medium_questions()
    return [{"description": q.description, "options": q.options} for q in questions]

@app.get("/questions/hard")
def get_hard():
    questions = get_hard_questions()
    return [{"description": q.description, "options": q.options} for q in questions]

