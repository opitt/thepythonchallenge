# the first trick is to consider .zip ... to download a file with content
# the second hint read the readme.txt inside the zip!
# then collect the comments inside the zip file ...

import zipfile

import re
from pathlib import Path

path = Path(__file__).with_name("channel.zip")
with zipfile.ZipFile(path, "r") as myzip:
    fname = "90052"
    comments = []

    while True:
        filename = f"{fname}.txt"
        zipinfo = myzip.getinfo(filename)
        comments.append(zipinfo.comment.decode("utf-8"))

        with myzip.open(filename, "r") as f:
            line = f.readline().decode("utf-8")
            m = re.search("is ([0-9]+)", line)
            if m:
                fname = m.group(1)
            else:
                print(f"{filename=}: {line=}")
                break

print("".join(comments))
sol = "hockey"

url_6 = "http://www.pythonchallenge.com/pc/def/channel.html"
url_7 = url_6.replace("channel", sol)

print(f"\nOpen now puzzle 7: {url_7}\n")
