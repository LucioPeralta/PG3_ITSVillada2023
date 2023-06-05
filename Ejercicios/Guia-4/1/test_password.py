import password

def test_validate_password():
    assert password.validate_password("Abc12345") == True
    assert password.validate_password("abc12345") == False
    assert password.validate_password("ABC12345") == False
    assert password.validate_password("abcABC123") == True
    assert password.validate_password("abc123456") == False

test_validate_password()