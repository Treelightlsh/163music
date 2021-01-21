import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# 生成RSAkey对象
rsa_key = RSA.construct((0x00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7, 0x10001))
# 生成加密器对象
cryptor = PKCS1_OAEP.new(rsa_key)
text = cryptor.encrypt(b'abc')
print(base64.encodebytes(text))