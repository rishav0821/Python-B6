import re
pattern = r"world"

text = "Hello world"
match = re.search(pattern, text)
print("Matched text:", match.group())
print("Start position:", match.start())
print("End position:", match.end())
