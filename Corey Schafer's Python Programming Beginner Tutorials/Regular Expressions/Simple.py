import re


text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

cat
mat
pat
bat

coreyms.com

321-555-4321
123.555.12 34
800-555-4321
900-555-4321


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")

matches = pattern.finditer(text_to_search)

# with open("/home/vitor/Python Scripts/Regular Expressions/data.txt", "r") as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

for match in matches:
    print(match)
