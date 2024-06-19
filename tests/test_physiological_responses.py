import pytest
from main import VoightKampffTest
from unittest.mock import patch


def test_physiological_responses_valid_input():
    vk_test = VoightKampffTest()
    with patch('builtins.input', side_effect=["15", "60", "2", "2"]):
        vk_test.physiological_responses()
    assert vk_test.user_responses["physiological_responses"]["breathing_rate"] == [
        15]
    assert vk_test.user_responses["physiological_responses"]["pulse_rate"] == [
        60]
    assert vk_test.user_responses["physiological_responses"]["blushing_intensity"] == [
        2]
    assert vk_test.user_responses["physiological_responses"]["pupil_dilation"] == [
        2]


def test_physiological_responses_invalid_input_breathing(capsys):
    vk_test = VoightKampffTest()
    with patch('builtins.input', side_effect=["100", "15", "60", "2", "2"]):
        vk_test.physiological_responses()
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
    assert vk_test.user_responses["physiological_responses"]["breathing_rate"] == [
        15]


def test_physiological_responses_invalid_input_pulse(capsys):
    vk_test = VoightKampffTest()
    with patch('builtins.input', side_effect=["15", "-200", "60", "2", "2"]):
        vk_test.physiological_responses()
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
    assert vk_test.user_responses["physiological_responses"]["pulse_rate"] == [
        60]


def test_physiological_responses_invalid_input_blushing(capsys):
    vk_test = VoightKampffTest()
    with patch('builtins.input', side_effect=["15", "60", "0", "2", "2"]):
        vk_test.physiological_responses()
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
    assert vk_test.user_responses["physiological_responses"]["blushing_intensity"] == [
        2]


def test_physiological_responses_invalid_input_pupil(capsys):
    vk_test = VoightKampffTest()
    with patch('builtins.input', side_effect=["15", "60", "2", "tutututuut", "2"]):
        vk_test.physiological_responses()
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
    assert vk_test.user_responses["physiological_responses"]["pupil_dilation"] == [
        2]
