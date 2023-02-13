import unicodedata
import random

def generate_nfc(s): #產出 NFC 字元
    return unicodedata.normalize('NFC', s)

def generate_nfd(s): #產出 NFD 字元
    return unicodedata.normalize('NFD', s)

def random_string(s): #隨機選出一個 s string 中的任一字元進行操作
    p = random.randint(0,16)
    return s[p]

s = "çàéùâêîôûäëïöüÿñ"

nfc_word = generate_nfc(random_string(s))
nfd_word = generate_nfd(random_string(s))

print("NFC encoded: ", nfc_word)
print("NFD encoded: ", nfd_word)