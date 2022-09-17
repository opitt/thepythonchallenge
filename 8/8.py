import bz2
import requests
import re

url_8 = "http://www.pythonchallenge.com/pc/def/integrity.html"

# un = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
# pw = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
# print(bz2.decompress(un).decode())
# print(bz2.decompress(pw).decode())

r = requests.get(url_8)
un, *_ = re.findall("(?<=un: .).*(?=.$)", r.text, re.MULTILINE)
pw, *_ = re.findall("(?<=pw: .).*(?=.$)", r.text, re.MULTILINE)
print(un, pw, sep="\n")

# un, *_ = codecs.escape_decode(bytes(un, "ascii"))
# ecoding/decoding with escape was inspired by https://stackoverflow.com/questions/27642198/bz2-decompress-with-python-3-4-typeerror-str-does-not-support-the-buffer-in
un = un.encode("latin1").decode("unicode_escape").encode("latin1")
pw = pw.encode("latin1").decode("unicode_escape").encode("latin1")

user = bz2.decompress(un).decode()
password = bz2.decompress(pw).decode()

url_9 = url_8.replace("def/integrity", "return/good")

print(f"\nOpen now puzzle 9: {url_9}\nUser: {user}\nPassword: {password}\n")
