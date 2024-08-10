import requests
import sys

url = sys.argv[1]
path = sys.argv[2]

wordlistFile = open(path, "r").readlines()

wordlist = []

for i in wordlistFile:
    wordlist.append(i.replace("\n", ""))

for dir in wordlist:
    response = requests.get(url + dir)
    print(f"Trying {url + dir}", end="\r")
    if response.status_code == 200:
        print(f"Found a valid page: {url + dir}")
