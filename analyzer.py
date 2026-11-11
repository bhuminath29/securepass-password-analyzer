import math
import re


COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "abc123"
}


def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS


def check_repeated_characters(password):
    return bool(re.search(r"(.)\1{3,}", password))


def check_sequences(password):
    weak_patterns = [
        "1234",
        "2345",
        "3456",
        "4567",
        "5678",
        "6789",
        "abcd",
        "bcde",
        "cdef",
        "qwerty"
    ]

    password_lower = password.lower()

    return any(
        pattern in password_lower
        for pattern in weak_patterns
    )


def calculate_entropy(password):
    pool_size = 0

    if any(char.islower() for char in password):
        pool_size += 26

    if any(char.isupper() for char in password):
        pool_size += 26

    if any(char.isdigit() for char in password):
        pool_size += 10

    if any(not char.isalnum() for char in password):
        pool_size += 32

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def analyze_password(password):

    length = len(password)

    has_uppercase = any(
        char.isupper() for char in password
    )

    has_lowercase = any(
        char.islower() for char in password
    )

    has_number = any(
        char.isdigit() for char in password
    )

    has_special = any(
        not char.isalnum() for char in password
    )

    is_common = check_common_password(password)

    has_repeated = check_repeated_characters(password)

    has_sequence = check_sequences(password)

    entropy = calculate_entropy(password)

    score = 0

    if length >= 8:
        score += 1

    if length >= 12:
        score += 1

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_number:
        score += 1

    if has_special:
        score += 1

    if is_common or has_repeated or has_sequence:
        score = min(score, 1)

    if score <= 1:
        strength = "Very Weak"

    elif score <= 2:
        strength = "Weak"

    elif score <= 3:
        strength = "Moderate"

    elif score <= 4:
        strength = "Strong"

    else:
        strength = "Very Strong"

    suggestions = []

    if length < 12:
        suggestions.append(
            "Use a longer password, preferably 12 or more characters."
        )

    if not has_uppercase:
        suggestions.append(
            "Include uppercase letters."
        )

    if not has_lowercase:
        suggestions.append(
            "Include lowercase letters."
        )

    if not has_number:
        suggestions.append(
            "Include numbers."
        )

    if not has_special:
        suggestions.append(
            "Include special characters."
        )

    if is_common:
        suggestions.append(
            "Avoid commonly used passwords."
        )

    if has_repeated:
        suggestions.append(
            "Avoid repeating the same character many times."
        )

    if has_sequence:
        suggestions.append(
            "Avoid predictable sequences and keyboard patterns."
        )

    if not suggestions:
        suggestions.append(
            "Your password meets all the checks in this tool. "
            "Use a unique password and consider a password manager."
        )

    return {
        "length": length,
        "uppercase": has_uppercase,
        "lowercase": has_lowercase,
        "number": has_number,
        "special": has_special,
        "common": is_common,
        "repeated": has_repeated,
        "sequence": has_sequence,
        "entropy": round(entropy, 2),
        "score": score,
        "strength": strength,
        "suggestions": suggestions
    }