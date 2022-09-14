# pip install pillow
from PIL import Image
from pathlib import Path

path = Path(__file__).with_name("oxygen.png")
message = [""]

with Image.open(path) as im:
    # im.show()
    w, h = im.size
    print(f"{w=} {h=}")
    px = im.load()

for x in range(w):
    p = px[(x, h // 2)]
    message.append(chr(p[0]))

msg = "".join(message)
print(f"{msg=}")

m = "".join(message[0:1] + message[5::7])
print(f"{m=}")

codes = m[m.index("[") + 1 : m.index("]")].split(", ")
print(f"{codes=}")

# the next level is ['105', '110', '116', '101', '103', '114', '105', '116', '121']
sol = "".join(chr(int(c)) for c in codes)
print(sol)

url_7 = "http://www.pythonchallenge.com/pc/def/oxygen.html"
url_8 = url_7.replace("oxygen", sol)

print(f"\nOpen now puzzle 8: {url_8}\n")
