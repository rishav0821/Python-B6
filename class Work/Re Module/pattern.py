import re

pattern = r"cat"

text = "The cat sat on the mat."
match = re.search(pattern, text)
print("Match found:", match.group() if match else "No match")
