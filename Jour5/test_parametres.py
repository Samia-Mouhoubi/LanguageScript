import pytest


def get_data():
    return [
        ("user1", "pass1"),
        ("user2", "pass2"),
        ("user3", "pass3"),
        ("user4", "pass4"),
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password):
    print(username,"---",password)




