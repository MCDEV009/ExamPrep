
import json

import csv
from datetime import datetime

def calculate_score(correct, total):
    if total <= 0:
        raise ValueError("Savollar soni musbat bo'lishi kerak")
    return round(correct / total * 100, 2)


def get_grade(score):
    if score >= 90:
        return "A'lo"
    elif score >= 70:
        return "Yaxshi"
    elif score >= 50:
        return "Qoniqarli"
    return "Ko'proq mashq qiling"


def ask_question(question_data):
    print("\n" + question_data["question"])

    for letter, option in question_data["options"].items():
        print(f"  {letter}) {option}")

    while True:
        answer = input("Javobingiz (A/B/C/D): ").strip().upper()
        if answer in question_data["options"]:
            break
        print("Noto'g'ri tanlov. A, B, C yoki D kiriting.")

    return answer == question_data["answer"].upper()


def load_questions(filename="questions.json"):
    with open(filename, "r", encoding="utf-8") as file:
        questions = json.load(file)

    if not questions:
        raise ValueError("Savollar fayli bo'sh")

    return questions


def run_quiz():
    questions = load_questions()
    correct = 0

    print("\n=== ExamPrep: Test boshlandi ===")

    for question in questions:
        if ask_question(question):
            print("To'g'ri!")
            correct += 1
        else:
            print(f"Noto'g'ri. To'g'ri javob: {question['answer']}")

    
    score = calculate_score(correct, len(questions))
    grade = get_grade(score)

    print("\n=== TEST NATIJASI ===")
    print(f"Jami savollar: {len(questions)}")
    print(f"To'g'ri javoblar: {correct}")
    print(f"Natija: {score}%")
    print(f"Baho: {grade}")

    with open("results.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "Sana", "Jami savollar",
                "To'g'ri javoblar", "Natija (%)", "Baho"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            len(questions), correct, score, grade
        ])

    print("Natija results.csv fayliga saqlandi.")
def main():
    while True:
        print("\n=== ExamPrep - Test dasturi ===")
        print("1. Testni boshlash")
        print("2. Chiqish")

        choice = input("Tanlang (1/2): ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("Dastur yakunlandi.")
            break
        else:
            print("Iltimos, 1 yoki 2 ni tanlang.")


if __name__ == "__main__":
    main()