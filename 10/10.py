url_10 = "http://www.pythonchallenge.com/pc/return/bull.html"

# a = [1, 11, 21, 1211, 111221,

from itertools import groupby

a = ["1"]
while len(a) < 31:
    next_a = "".join([f"{len(list(v))}{k}" for k, v in groupby(a[-1])])
    a.append(next_a)

sol = len(a[30])  # 5808
url_11 = url_10.replace("bull", str(sol))

print(f"\nOpen now puzzle 11: {url_11}\n")
