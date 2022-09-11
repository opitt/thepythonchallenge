table = "".maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = text.translate(table)

print(text.replace(". ", ".\n"))

url_1 = "http://www.pythonchallenge.com/pc/def/map.html"
url_2 = url_1.replace("map", "map".translate(table))

print(f"\nOpen now puzzle 2: {url_2}\n")
