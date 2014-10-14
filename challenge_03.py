# ------------
# Challenge 03
# ------------

import urllib2
import re
import links
from base64 import b64decode

# Obfuscated to avoid spoilers
url = b64decode(links.link_03)

# Message is huge, so using urllib2 instead of copy/paste
response = urllib2.urlopen(url)
html = response.read()

# Quick extraction of message from html
msg = html.split('--')[-2].strip('\n')

# Still in progress....