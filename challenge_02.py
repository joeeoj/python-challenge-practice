# ------------
# Challenge 02
# ------------

import urllib2
from base64 import b64decode
import links

# Obfuscated to avoid spoilers
url = b64decode(links.link_02)

# Message is huge, so using urllib2 instead of copy/paste
response = urllib2.urlopen(url)
html = response.read()

# Quick extraction of message from html
msg = html.split('--')[-2].strip('\n')

base_url = 'http://www.pythonchallenge.com/pc/def/{}.html'
decoded = ''.join([c for c in msg if c.isalpha()])

print 'The secret message is', decoded
print base_url.format(decoded)