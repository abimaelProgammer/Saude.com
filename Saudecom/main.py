import os

os.chdir("./projeto")
os.system("python3 -m http.server 8080 --cgi")