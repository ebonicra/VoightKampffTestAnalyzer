import pytest
from main import VoightKampffTest
from unittest.mock import patch


def test_ask_question_valid_input_1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    vk_test = VoightKampffTest()
    question = "Вопрос 1?"
    answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"]
    assert vk_test.ask_question(question, answers) == 1


def test_ask_question_valid_input_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2")
    vk_test = VoightKampffTest()
    question = "Вопрос 2?"
    answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"]
    assert vk_test.ask_question(question, answers) == 2


def test_ask_question_valid_input_4(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4")
    vk_test = VoightKampffTest()
    question = "Вопрос 4?"
    answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"]
    assert vk_test.ask_question(question, answers) == 4


def test_ask_question_invalid_input_negative(capsys):
    vk_test = VoightKampffTest()
    question = "Вопрос?"
    answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"]
    with patch('builtins.input', side_effect=["-4", "1"]):
        vk_test.ask_question(question, answers)
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out


def test_ask_question_invalid_input_0(capsys):
    vk_test = VoightKampffTest()
    question = "Вопрос?"
    answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"]
    with patch('builtins.input', side_effect=["0", "1"]):
        vk_test.ask_question(question, answers)
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out


def test_ask_question_invalid_input_555(capsys):
    vk_test = VoightKampffTest()
    question = "Вопрос?"
    answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"]
    with patch('builtins.input', side_effect=["555", "1"]):
        vk_test.ask_question(question, answers)
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out


def test_ask_question_invalid_input_text(capsys):
    vk_test = VoightKampffTest()
    question = "Вопрос?"
    answers = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"]
    with patch('builtins.input', side_effect=["ttttt", "1"]):
        vk_test.ask_question(question, answers)
    captured = capsys.readouterr()
    assert "Ошибка:" in captured.out
