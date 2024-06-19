import pytest
from main import VoightKampffTest


def test_load_questions_empty_file():
    test = VoightKampffTest()
    with pytest.raises(ValueError):
        test.load_questions('empty_questions.json')


def test_load_questions_nonexistent_file():
    test = VoightKampffTest()
    with pytest.raises(FileNotFoundError):
        test.load_questions('nonexistent_file.json')


def test_load_questions_invalid_format():
    test = VoightKampffTest()
    with pytest.raises(ValueError):
        test.load_questions('invalid_format_questions.json')


def test_load_questions_valid_file():
    test = VoightKampffTest()
    questions = test.load_questions('valid_questions.json')
    assert isinstance(questions, list)
    assert len(questions) > 0
    assert all(isinstance(q, dict) for q in questions)
    assert all('question' in q and 'answers' in q for q in questions)
