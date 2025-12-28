import pytest
import sys
from attendance import calculate_attendance_percentage, get_exam_eligibility

def test_percentage():
    assert calculate_attendance_percentage(100, 80) == 80.0

def test_eligible():
    assert get_exam_eligibility(80) == "Eligible for Exam"

def test_not_eligible():
    assert get_exam_eligibility(60) == "Not Eligible for Exam"

def test_invalid_total():
    with pytest.raises(ValueError):
        calculate_attendance_percentage(0, 10)
