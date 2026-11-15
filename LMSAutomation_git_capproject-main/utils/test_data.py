class TestData:
    VALID_USER = ("student1", "Pass123!")

    INVALID_USERS = [
        ("wrong_user", "Pass123!"),
        ("student1", "wrong_pass"),
        ("", "Pass123!"),
        ("student1", ""),
    ]
