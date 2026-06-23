import re

def get_store_name(lines): 

    for line in lines:
        if line.strip():    # The first non-empty line
            return line.strip()
    return "Unknown"

def get_date(lines):

    pattern = r"\b\d{2}[/-]\d{2}[/-]\d{2,4}\b"

    for line in lines:
        match = re.search(pattern, line)
        if match:
            return match.group()   # group() returns the actual matched text.

    return "Not Found"


def total_amount(lines):

    keywords = ["total", "grand total", "amount"]

    for line in lines:
        lower = line.lower()

        if any(word in lower for word in keywords):
            amount = re.findall(r"\d+\.\d{2}|\d+", line)

            if amount:
                return amount[-1]

    return "Not Found"