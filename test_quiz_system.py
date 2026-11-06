import pytest
from quiz_system import Question, QuizManagementSystem


@pytest.fixture
def qms():
    system = QuizManagementSystem("Python Basics Quiz")
    system.add_question(Question(1, "Which data type is mutable?", ["List", "Tuple", "String"], "List"))
    system.add_question(Question(2, "Which keyword defines a function?", ["func", "def", "define"], "def"))
    system.add_question(Question(3, "What is the output of 2 ** 3?", ["6", "8", "9"], "8"))
    return system


def test_questions_are_added(qms):
    assert len(qms.questions) == 3


def test_full_score_passes(qms, capsys):
    assert qms.evaluate("Alice", {1: "List", 2: "def", 3: "8"}) == 3
    assert "Result: Pass" in capsys.readouterr().out


def test_low_score_fails(qms, capsys):
    assert qms.evaluate("Bob", {1: "Tuple", 2: "def", 3: "6"}) == 1
    assert "Result: Fail" in capsys.readouterr().out


def test_unanswered_questions_score_zero(qms):
    assert qms.evaluate("Carol", {}) == 0


def test_list_questions_prints_every_option(qms, capsys):
    qms.list_questions()
    out = capsys.readouterr().out
    assert "Q3. What is the output of 2 ** 3?" in out and "3) 9" in out
