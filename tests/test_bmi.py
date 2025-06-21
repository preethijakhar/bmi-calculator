from app.bmi import calculate_bmi


def test_bmi():
    assert calculate_bmi(70, 1.75) == 22.86
