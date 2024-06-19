BREATHING_JUMP = 3
PULSE_JUMP = 20
BLUSHING_JUMP = 2
PUPIL_JUMP = 2


def analyze_physiological_responses(physiological_responses: dict[str, list[float]]) -> str:
    """Analyzes physiological responses to determine whether the user is human or replicant.

    :param physiological_responses: A dictionary containing physiological responses recorded during the test.
                                     It should have keys: 'breathing_rate', 'pulse_rate', 'blushing_intensity',
                                     'pupil_dilation', each mapped to a list of corresponding float values.
    :return: A string indicating whether the user is a human or a replicant.
    """
    has_breathing_jump = False
    has_pulse_jump = False
    has_blushing_jump = False
    has_pupil_jump = False

    for key, values in physiological_responses.items():
        for i in range(1, len(values)):
            if key == 'breathing_rate' and abs(values[i] - values[i-1]) >= BREATHING_JUMP:
                has_breathing_jump = True
            elif key == 'pulse_rate' and abs(values[i] - values[i-1]) >= PULSE_JUMP:
                has_pulse_jump = True
            elif key == 'blushing_intensity' and abs(values[i] - values[i-1]) >= BLUSHING_JUMP:
                has_blushing_jump = True
            elif key == 'pupil_dilation' and abs(values[i] - values[i-1]) >= PUPIL_JUMP:
                has_pupil_jump = True

    if has_breathing_jump and has_pulse_jump and has_blushing_jump and has_pupil_jump:
        return 'ЧЕЛОВЕК!'
    else:
        return 'РЕПЛИКАНТ!'
