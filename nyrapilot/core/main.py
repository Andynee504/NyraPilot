import time
from .timer import StudyTimer
from .transcribe import transcribe_audio
from dotenv import load_dotenv
import datetime
import csv
import os
from pathlib import Path

# Carregar .env
load_dotenv()

# Alternar entre modo online e offline
modo_teste = os.getenv("NYRA_TEST_MODE", "false").lower() == "true"
if modo_teste:
    from .analyzer_offline import analyze_content
else:
    from .analyzer import analyze_content

LOG_FILE = Path("logs/study_log.csv")
GOAL_FILE = Path("config/goal.txt")

def ask_user_info():
    print("\nLet's record this study session.")
    course = input("Nome do course: ").strip()
    chapter = input("Chapter or module: ").strip()
    lesson = input("Número da lesson na ordem do course: ").strip()
    data = datetime.date.today().isoformat()
    return course, chapter, lesson, data

def save_log(course, chapter, lesson, data, duration):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    exists = LOG_FILE.exists()
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["Curso", "Capítulo", "Aula (nº)", "Date", "Study Time (min)"])
        writer.writerow([course, chapter, lesson, data, round(duration / 60, 2)])

def main():
    print("Hello, I’m Nyra. Estou pronta para te ajudar a focar no que importa.")
    input("Pressione Enter quando a lesson começar...")

    timer = StudyTimer()
    timer.start()

    print("Starting transcription...")
    texto = transcribe_audio("audio_temp.wav")

    print("Analisando com base no seu goal atual...\n")
    with open(GOAL_FILE, "r", encoding="utf-8") as f:
        goal = f.read()
    response = analyze_content(goal, texto)
    print("Nyra diz:")
    print(response)
    print()

    timer.stop()

    course, chapter, lesson, data = ask_user_info()
    save_log(course, chapter, lesson, data, timer.elapsed_time())

    print(f"Study session successfully logged. Active time: {round(timer.elapsed_time() / 60, 2)} minutos.")

if __name__ == "__main__":
    main()
