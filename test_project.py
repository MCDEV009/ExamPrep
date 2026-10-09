
import json
import pytest

from project import calculate_score, get_grade, load_questions


def test_calculate_score():
    assert calculate_score(8, 10) == 80.0
    assert calculate_score(5, 5) == 100.0
    assert calculate_score(0, 10) == 0.0


def test_calculate_score_invalid_total():
    with pytest.raises(ValueError):
        calculate_score(0, 0)


def test_get_grade():
    assert get_grade(95) == "A'lo"
    assert get_grade(75) == "Yaxshi"
    assert get_grade(55) == "Qoniqarli"
    assert get_grade(30) == "Ko'proq mashq qiling"


def test_load_questions(tmp_path):
    questions = [
        {
            "question": "2 + 2 nechaga teng?",
            "options": {
                "A": "3",
                "B": "4",
                "C": "5",
                "D": "6"
            },
            "answer": "B"
        }
    ]

    file_path = tmp_path / "questions.json"
    file_path.write_text(
        json.dumps(questions, ensure_ascii=False),
        encoding="utf-8"
    )

    result = load_questions(str(file_path))
    assert len(result) == 1
    assert result[0]["answer"] == "B"