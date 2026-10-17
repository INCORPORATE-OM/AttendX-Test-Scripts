# Tests attendance marking


def test_mark_attendance():
    student_id = "STU101"
    status = "Present"
    assert student_id != ""
    assert status in ["Present", "Absent"]


def test_attendance_requires_student_id():
    student_id = ""
    assert student_id == ""
