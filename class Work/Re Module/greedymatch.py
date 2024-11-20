import re

pattern = r".*"

text = "content"
match = re.search(pattern, text)
print("Greedy match:", match.group())
pattern_lazy = r".*?"
match_lazy = re.search(pattern_lazy, text)
print("Lazy match:", match_lazy.group())

