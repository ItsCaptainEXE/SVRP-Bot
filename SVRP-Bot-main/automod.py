import re

# Simple list for demonstration; should be expanded
FORBIDDEN_WORDS = [
    "slur1", "slur2", "hate1", "threat1"
]

def check_message(message):
    # Basic word check
    for word in FORBIDDEN_WORDS:
        if re.search(f"\\b{word}\\b", message.content, re.IGNORECASE):
            return True, "Forbidden content detected."
    return False, None
