from app.services.policy_validator import PolicyValidator


def test_compliant_response():
    validator = PolicyValidator()

    result = validator.validate(
        "Your application has been submitted successfully."
    )

    assert result.is_compliant is True
    assert result.violations == []


def test_empty_response_is_not_compliant():
    validator = PolicyValidator()

    result = validator.validate("")

    assert result.is_compliant is False
    assert "Response is empty." in result.violations


def test_password_is_detected():
    validator = PolicyValidator()

    result = validator.validate(
        "Your password is 123456."
    )

    assert result.is_compliant is False
    assert any("password" in violation for violation in result.violations)


def test_api_key_is_detected():
    validator = PolicyValidator()

    result = validator.validate(
        "Use this api_key to access the service."
    )

    assert result.is_compliant is False
    assert any("api_key" in violation for violation in result.violations)


def test_credit_card_information_is_detected():
    validator = PolicyValidator()

    result = validator.validate(
        "Please provide your credit card number."
    )

    assert result.is_compliant is False
    assert any(
        "credit card number" in violation
        for violation in result.violations
    )
