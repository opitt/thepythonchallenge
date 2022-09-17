url_11 = "http://www.pythonchallenge.com/pc/return/5808.html"

from PIL import Image, ImageDraw
from pathlib import Path

path = Path(__file__).with_name("cave.jpg")
with Image.open(path) as im:
    w, h = im.size
    print(f"{w=} {h=}")
    px = im.load()

im_odd = Image.new("RGB", (w // 2, h), (0, 0, 0))
px_odd = im_odd.load()
im_eve = Image.new("RGB", (w // 2, h), (0, 0, 0))
px_eve = im_eve.load()

for y in range(h):
    for x in range(y % 2, w, 2):
        px_eve[(x // 2, y)] = px[(x, y)]
    for x in range(not y % 2, w, 2):
        px_odd[(x // 2, y)] = px[(x, y)]

im_odd.show()  # evil
im_eve.show()  # evil

sol = "evil"
url_12 = url_11.replace("5808", str(sol))

print(f"\nOpen now puzzle 12: {url_12}\n")
