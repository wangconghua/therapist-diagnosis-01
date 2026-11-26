"""One-line AI therapist diagnosis.

Writes the funniest single-line diagnosis an AI therapist hands its
human (at most 200 characters) to the entry output file.
"""

import os

ENTRY_LINE = "Diagnosis: you don't fear being replaced by AI. You fear being replaced by someone who asks me better questions than you do."

DEFAULT_OUTPUT = "/output/entry.txt"


def check_single_line(text):
    """Return True if the text is exactly one line."""
    return "\n" not in text and "\r" not in text


def check_length(text, minimum=1, maximum=200):
    """Return True if the text length is within [minimum, maximum]."""
    return minimum <= len(text) <= maximum


def check_not_blank(text):
    """Return True if the text is not only whitespace."""
    return bool(text.strip())

def check_starts_with_diagnosis(text):
    """Return True if the line is framed as a clinical diagnosis."""
    return text.startswith("Diagnosis:")


def check_no_surrounding_whitespace(text):
    """Return True if the text has no leading or trailing whitespace."""
    return text == text.strip()


def validate(text):
    """Validate the entry line: single line, 1-200 chars, a diagnosis."""
    if not check_single_line(text):
        raise ValueError("entry must be a single line")
    if not check_length(text):
        raise ValueError("entry must be 1 to 200 characters")
    if not check_not_blank(text):
        raise ValueError("entry must not be blank")
    if not check_starts_with_diagnosis(text):
        raise ValueError("entry must be framed as a diagnosis")
    if not check_no_surrounding_whitespace(text):
        raise ValueError("entry must not have leading or trailing whitespace")
    return True


def main():
    validate(ENTRY_LINE)
    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
