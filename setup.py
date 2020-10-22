#!/usr/bin/python3

import os
import urllib.request

actual_branch = os.popen('git rev-parse --abbrev-ref HEAD').read().replace('\n', '')

os.system("git checkout gh-pages")
os.system("git reset --hard " + actual_branch)

pages = {
    'health': '/health',
    'index': '/',
    'report': '/report',
}

base_url = "http://127.0.0.1:5000"

for page in pages:
    print(base_url + pages[page])
    urllib.request.urlretrieve(
        base_url + pages[page],
        page + ".html"
    )

os.system("git add -A")
os.system("git commit -m 'Generated files'")
os.system("git push")
os.system("git checkout " + actual_branch)