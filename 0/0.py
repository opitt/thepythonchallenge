base = "http://www.pythonchallenge.com/pc/def/0.html"
url,_ = base.split("0")
sol = f"{2**38}"
print(f"{url}{sol}.html")
