import pyperclip
import re

def extract_email_and_text():
    email_regex = re.compile('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,4}')
    phone_regex = re.compile('(?:\+1)?\s?\d{3}[-.]\d{3}[-.]\d{4}')

    text = str(pyperclip.paste())
    matches = []

    if text:
        emails = email_regex.findall(text)
        numbers = phone_regex.findall(text)

        for email in emails:
            matches.append(email)

        for number in numbers:
            matches.append(number)

    if len(matches) > 0:
        matches_str = '\n'.join(matches)
        pyperclip.copy(matches_str)
        print(matches_str)

extract_email_and_text()
