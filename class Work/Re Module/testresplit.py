#write a function that takes a string with email and returnit with email enclosed in bold tag

import re
test = """
This is my email rishav.18271@stu.upes.ac.in

"""
def bold_email(test):

    pattern_email = r"[\w.]+@[\S]*"
    match = re.search(pattern_email,test)
    print(f"\n\n{match.group()}\n\n")
    replace = f"<b>{ match.group() }</b>"
    replacedString = re.sub(pattern_email,replace,test)
    return replacedString

replacedString = bold_email(test)
print("after replacement")
print(f"\n\n{replacedString}\n\n")