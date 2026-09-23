from dataclasses import dataclass, field
from typing import List


@dataclass
class ValidationResult:
    is_valid: bool
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class ResponseValidator:
    """Validates AI responses against basic quality and safety rules."""

    CONFIDENTIAL_PATTERNS = (
        "api_key",
        "secret_key",
        "password=",
        "authorization: bearer",
        "private_key",
    )

    def validate(self, response: str) -> ValidationResult:
        issues: List[str] = []
        warnings: List[str] = []

        if not response or not response.strip():
            issues.append("Response is empty.")
            return ValidationResult(False, issues, warnings)

        normalized = response.lower()

        for pattern in self.CONFIDENTIAL_PATTERNS:
            if pattern in normalized:
                issues.append("Response may contain confidential information.")
                break

        if len(response.strip()) < 10:
            warnings.append("Response is unusually short.")

        return ValidationResult(
            is_valid=len(issues) == 0,
            issues=issues,
            warnings=warnings,
        )


response_validator = ResponseValidator()
