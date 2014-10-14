# ------------
# Challenge 01
# ------------

import string


base_url = 'http://www.pythonchallenge.com/pc/def/{}.html'

# Watch out for the hidden single quote!
msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

from_trans = string.ascii_lowercase
# Caesar shift two chars to the right
to_trans = from_trans[2:] + from_trans[0:2]

decoder = string.maketrans(from_trans, to_trans)

print "Decoded message:", string.translate(msg, decoder)
print base_url.format(string.translate(next_challenge, decoder))