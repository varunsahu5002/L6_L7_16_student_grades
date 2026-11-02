import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# ---- letter_grade: every branch + boundaries ----
@pytest.mark.parametrize("marks, expected", [
    (100, "S"), (90, "S"),
    (89, "A"), (80, "A"),
    (79, "B"), (70, "B"),
    (69, "C"), (60, "C"),
    (59, "D"), (50, "D"),
    (49, "E"), (40, "E"),
    (39, "F"), (0, "F"),
])
def test_letter_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected

def test_letter_grade_negative():
    with pytest.raises(ValueError):
        letter_grade(-1)

def test_letter_grade_above_100():
    with pytest.raises(ValueError):
        letter_grade(101)


# ---- final_marks ----
def test_internal_too_high():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)

def test_external_too_high():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)

def test_no_project():
    assert final_marks(30, 40, False) == 70

def test_project_below_cap():
    assert final_marks(30, 40, True) == 75

def test_project_exactly_100():
    assert final_marks(40, 55, True) == 100

def test_project_capped():
    assert final_marks(40, 60, True) == 100

def test_final_marks_max_boundaries_no_error():
    assert final_marks(40, 60, False) == 100


# ---- exam_eligibility ----
def test_fees_not_paid():
    assert exam_eligibility(90, False, True) == "blocked"

def test_attendance_75_exact():
    assert exam_eligibility(75, True, False) == "eligible"

def test_attendance_high():
    assert exam_eligibility(80, True, False) == "eligible"

def test_medical_condonation_eligible():
    assert exam_eligibility(65, True, True) == "eligible"

def test_mid_attendance_no_medical():
    assert exam_eligibility(70, True, False) == "detained"

def test_low_attendance_with_medical():
    assert exam_eligibility(64, True, True) == "detained"

def test_low_attendance_no_medical():
    assert exam_eligibility(40, True, False) == "detained"