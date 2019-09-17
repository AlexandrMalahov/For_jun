"""Validating postal codes. Difficulty: Hard."""

import re

regex_integer_in_range = r"\b[1-9]\d{5}\b"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
P = input()
print(
    bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)
