import re
import requests
import subprocess
import os

print("\x1bc\x1b[43;30m")

page = requests.get("https://godbolt.org/")

ss="<html><head><title>hello</title></head><body><iframe src='https://godbolt.org/' width='1800' height='1600'></iframe></body></html>"
f1=open("c.html","w")
f1.write(ss)
f1.close()
os.system("start .\c.html")


