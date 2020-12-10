import re

regex_pattern = r"[^0-9]"
print("\n".join(re.split(regex_pattern, input())))