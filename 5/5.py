from pickle import load
from pathlib import Path

pth = Path(__file__).with_name("banner.p")
with pth.open("rb") as pickle_file:
    src = load(pickle_file)
    print(src)

for line in src:
    print("".join(list(map(lambda t: t[0] * t[1], line))))

url_5 = "http://www.pythonchallenge.com/pc/def/peak.html"
sol = "channel"
url_6 = url_5.replace("peak", sol)

print(f"\nOpen now puzzle 6: {url_6}\n")
