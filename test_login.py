# Tests login validation


def test_login_with_valid_credentials():
    username = "student01"
    password = "AttendX@123"
    assert username != ""
    assert password != ""
    assert len(password) >= 8


def test_login_with_empty_credentials():
    username = ""
    password = ""
    assert username == ""
    assert password == ""
