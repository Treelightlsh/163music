"""
通过浏览器调试分析，得知抓取网易云音乐需要在post请求中，获取表单参数encSecKey
和params，其实歌曲id就隐藏在里面
"""
import random
import base64
# AES加密导入
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

param1 = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_189315",
    "threadid": "R_SO_4_189315"
}
param2 = "010001"
param3 = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
param4 = "0CoJUm6Qyw8W8jud"


def get_16_bit_char(length):
    """随机生成一个length位的字符串"""
    # 备选字符
    res = ''
    c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(length):
        res = res + random.choice(c)
    return res


def to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return text


def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)


def AES_encrypt(text, key, iv):  # text为密文，key为公钥，iv为偏移量
    bs = AES.block_size
    pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    encryptor = AES.new(to_16(key), AES.MODE_CBC, to_16(iv))
    # 转换成字节序列(bytes)，再加密
    encrypt_aes = encryptor.encrypt(str.encode(pad2(text)))
    # 用base64位编码，然后转换成字符串
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypt_text


def get_params(text, key1, key2, iv):
    enc_text1 = AES_encrypt(text, key1, iv)
    enc_text2 = AES_encrypt(enc_text1.strip(), key2, iv)
    return enc_text2


# a = '{"rid":"R_SO_4_189315","threadId":"R_SO_4_189315","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
a = '{"csrf_token":""}'
key1 = "0CoJUm6Qyw8W8jud"
key2 = "w9dGE3JbTy1uBUMB"
iv = '0102030405060708'
# print(AES_encrypt("eHhjXckqrtZkqcwCalCMx0QuU6Lj9L7Wxouw1iMCnB4=", key2, iv))
print(get_params(a, key1, key2, iv))
# "eHhjXckqrtZkqcwCalCMx0QuU6Lj9L7Wxouw1iMCnB4="
# "3nQlVaXJDAupLmemo7mzgMD3Ajva26v9SXhKohnk2HVHXQBvkZlA1mkcmYae6EYZ"
