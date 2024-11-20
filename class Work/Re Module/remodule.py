import re
pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
print("Match found:", match.group() if match else "No match")
