import requests
import tkinter

url = "http://14.225.36.152:10106/api?region=dev_docker&ticket=GM&cmd=1116&uid={}&msg={}"

uid = input("nhập uid:")

command = input("nhập command:")

response = requests.get(url.format(uid, command))

print(response.status_code)
print(response.headers)
print(response.text)
