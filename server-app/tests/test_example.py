def get_welcome_message(is_authenticated: bool) -> dict:
    if is_authenticated:
        return {"message": "Welcome to the Finance API"}
    else:
        return {"error": "Authentication required"}


def test_get_welcome_message_pass():
    # Pass case: User is authenticated
    result = get_welcome_message(is_authenticated=True)
    assert result == {"message": "Welcome to the Finance API"}

def test_get_welcome_message_fail():
    # Fail case: Deliberately incorrect expectation to simulate a failing test
    result = get_welcome_message(is_authenticated=False)
    assert result == {"message": "Welcome to the Finance API"}  # This will fail

