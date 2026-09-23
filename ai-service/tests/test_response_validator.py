from app.services.response_validator import ResponseValidator


def test_valid_response():
    validator = ResponseValidator()

    result = validator.validate(
        "Your application has been successfully submitted."
    )

    assert result.is_valid is True
    assert result.issues == []


def test_empty_response_is_invalid():
    validator = ResponseValidator()

    result = validator.validate("")

    assert result.is_valid is False
    assert "Response is empty." in result.issues


def test_confidential_information_is_detected():
    validator = ResponseValidator()

    result = validator.validate(
        "Your api_key is api_key=abc123."
    )

    assert result.is_valid is False
    assert "Response may contain confidential information." in result.issues


def test_short_response_generates_warning():
    validator = ResponseValidator()

    result = validator.validate("Okay")

    assert result.is_valid is True
    assert "Response is unusually short." in result.warnings
