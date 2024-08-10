# Directory Bruteforce Script

This Python script is a simple directory brute-forcing tool. It takes a URL and a wordlist file as input, then attempts to find valid directories on the specified website. The script will make HTTP requests to the target URL with each directory name from the wordlist and report if a valid directory is found.


**Usage** : python script.py <url> <wordlist.txt>

**Usage example**: python script.py https://example.com/ wordlist.txt

**How It Works**
The script reads a wordlist file containing potential directory names.
It iterates through each directory name, appending it to the target URL.
An HTTP GET request is sent to the URL+directory.
If the response status code is 200, it indicates that the directory exists, and the script will print the directory's full URL.
