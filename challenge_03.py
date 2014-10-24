# ------------
# Challenge 03
# ------------

import urllib2
import re
import links
from base64 import b64decode

base = 'http://www.pythonchallenge.com/pc/def/{}.html'

# Obfuscated to avoid spoilers
url = b64decode(links.link_03)

# Message is huge, so using urllib2 instead of copy/paste
response = urllib2.urlopen(url)
html = response.read()

# Quick extraction of message from html
msg = html.split('--')[-2].strip('\n')

# First attempt at python regex
pattern = re.compile(r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')

result = re.findall(pattern, msg)
ans = ''.join([pat[4] for pat in result])

print base.format(ans)
