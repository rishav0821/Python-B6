import re

pattern = r"\s+"

text = "Split this sentence by spaces"
result = re.split(pattern, text)
print("Split result:", result)
