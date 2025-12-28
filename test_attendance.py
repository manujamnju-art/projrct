from attendance import calculate_attendance_percentage, get_exam_eligibility

def test_attendance_percentage():
    assert calculate_attendance_percentage(75, 100) == 75.0

def test_exam_eligibility():
    assert get_exam_eligibility(80) == "Eligible"
    assert get_exam_eligibility(60) == "Not Eligible"
