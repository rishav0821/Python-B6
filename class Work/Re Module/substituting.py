import re
pattern = r"cat"

text = "The cat sat on the mat."
result = re.sub(pattern, "dog", text)
print("After substitution:", result)
