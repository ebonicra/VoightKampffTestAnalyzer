import pytest
from main import VoightKampffTest, analyze_physiological_responses


@pytest.mark.parametrize("user_input", [
    ["Test User", 1, 12, 60, 2, 2, 4, 16, 100, 6, 6]
])
def test_voight_kampff_person(monkeypatch, user_input):
    user_input_iter = iter(user_input)
    monkeypatch.setattr('builtins.input', lambda _: str(next(user_input_iter)))
    vk_test = VoightKampffTest()
    vk_test.welcome_user()
    questions_data = [
        {"question": "Question 1", "answers": {"1": "Answer 1",
                                               "2": "Answer 2", "3": "Answer 3", "4": "Answer 4"}},
        {"question": "Question 2", "answers": {"1": "Answer 1",
                                               "2": "Answer 2", "3": "Answer 3", "4": "Answer 4"}}
    ]
    vk_test.record_responses(questions_data)
    vk_test.save_user_responses()
    vk_test.analyze_user_responses()
    assert vk_test.user_responses["user"] == "Test User"
    assert len(vk_test.user_responses["responses"]) == 2
    assert len(
        vk_test.user_responses["physiological_responses"]["breathing_rate"]) == 2
    assert analyze_physiological_responses(
        vk_test.user_responses["physiological_responses"]) == "ЧЕЛОВЕК!"


@pytest.mark.parametrize("user_input_invalid", [
    ["Test User", 1, 12, 60, 2, 2, 1, 12, 60, 2, 2]
])
def test_voight_kampff_replicant(monkeypatch, user_input_invalid):
    user_input_iter = iter(user_input_invalid)
    monkeypatch.setattr('builtins.input', lambda _: str(next(user_input_iter)))
    vk_test = VoightKampffTest()
    vk_test.welcome_user()
    questions_data = [
        {"question": "Question 1", "answers": {"1": "Answer 1",
                                               "2": "Answer 2", "3": "Answer 3", "4": "Answer 4"}},
        {"question": "Question 2", "answers": {"1": "Answer 1",
                                               "2": "Answer 2", "3": "Answer 3", "4": "Answer 4"}}
    ]
    vk_test.record_responses(questions_data)
    vk_test.save_user_responses()
    vk_test.analyze_user_responses()
    assert vk_test.user_responses["user"] == "Test User"
    assert len(vk_test.user_responses["responses"]) == 2
    assert len(
        vk_test.user_responses["physiological_responses"]["breathing_rate"]) == 2
    assert analyze_physiological_responses(
        vk_test.user_responses["physiological_responses"]) == "РЕПЛИКАНТ!"
