from dataclasses import dataclass, field
from typing import List


@dataclass
class PolicyValidationResult:
    is_compliant: bool
    violations: List[str] = field(default_factory=list)


class PolicyValidator:
    """Checks AI responses against configurable policy rules."""

    BLOCKED_PATTERNS = (
        "password",
        "api_key",
        "secret_key",
        "private_key",
        "credit card number",
    )

    def validate(self, response: str) -> PolicyValidationResult:
        violations: List[str] = []

        if not response or not response.strip():
            violations.append("Response is empty.")
            return PolicyValidationResult(False, violations)

        normalized = response.lower()

        for pattern in self.BLOCKED_PATTERNS:
            if pattern in normalized:
                violations.append(
                    f"Response contains potentially restricted content: {pattern}."
                )

        return PolicyValidationResult(
            is_compliant=len(violations) == 0,
            violations=violations,
        )


policy_validator = PolicyValidator()
