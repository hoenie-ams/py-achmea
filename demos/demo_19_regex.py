import re

text = "The year was 1999 and all the systems were about to break."
pattern = r"\d{4}"

result = re.search(pattern, text)


text = "The user's e-mail address is john@doe.com"
pattern = r"\S+@\S+\.(com|nl|be)"

text = "john@doe.com"
pattern = r"(\S+)@(\S+\.(com|nl|be))"
result = re.search(pattern, text)
