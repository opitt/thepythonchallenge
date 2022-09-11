import requests
import re

#nothing = "12345" # start with what is given in the page source: ... does not work
nothing = "1"

for step in range(400):
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
    text = requests.get(url).text
    print(f"{step:03}: {url} ... {text}")
    # The page we look for contains: "and the next nothing is 66248"
    # if not, then we reached possibly the end of the chain ...
    pattern = ".*nothing is ([0-9]+$)"
    m = re.match(pattern, text, flags=re.MULTILINE)
    if m:
        nothing = m.group(1)
    else:
        print(f"\nPossible end of linked list found:\n{url}\n{text=}")
        break
else:
    print("Not on the right path ...")

if step < 400:
    url_5, _ = url.split("linked")
    url_5 += text

    print(f"\nOpen now puzzle 5: {url_5}\n")
